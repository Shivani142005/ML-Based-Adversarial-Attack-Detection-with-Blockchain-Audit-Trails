import torch
import torch.nn.functional as F
from models.autoencoder import Autoencoder

torch.manual_seed(42)


class AdversarialDetector:
    def __init__(self, model, device="cpu"):
        self.model = model.to(device)
        self.device = device
        self.model.eval()

        # Autoencoder (only for reconstruction error monitoring)
        self.autoencoder = Autoencoder().to(device)
        self.autoencoder.load_state_dict(
            torch.load("models/saved/autoencoder.pth", map_location=device)
        )
        self.autoencoder.eval()

    def entropy(self, prob):
        return -torch.sum(prob * torch.log(prob + 1e-8), dim=1)

    def detect(self, image):
        image = image.to(self.device)

        # -------------------------------
        # ORIGINAL PREDICTION
        # -------------------------------
        with torch.no_grad():
            out1 = self.model(image)
            prob1 = F.softmax(out1, dim=1)
            conf1, pred1 = torch.max(prob1, 1)
            entropy1 = self.entropy(prob1)

        # -------------------------------
        # INTERNAL FGSM TEST (WEAK - SAFE)
        # -------------------------------
        image_adv = image.clone().detach().requires_grad_(True)

        out = self.model(image_adv)
        loss = F.cross_entropy(out, pred1)

        self.model.zero_grad()
        loss.backward()

        # 🔥 reduced epsilon (IMPORTANT)
        adv = image_adv + 0.02 * image_adv.grad.sign()
        adv = torch.clamp(adv, -1, 1)

        with torch.no_grad():
            out_adv = self.model(adv)
            prob_adv = F.softmax(out_adv, dim=1)
            conf_adv, pred_adv = torch.max(prob_adv, 1)

        # -------------------------------
        # SMALL NOISE TEST (VERY LIGHT)
        # -------------------------------
        noise = torch.randn_like(image) * 0.01
        noisy = torch.clamp(image + noise, -1, 1)

        with torch.no_grad():
            out2 = self.model(noisy)
            prob2 = F.softmax(out2, dim=1)
            conf2, pred2 = torch.max(prob2, 1)
            entropy2 = self.entropy(prob2)

        # -------------------------------
        # METRICS
        # -------------------------------
        drop_fgsm = abs(conf1.item() - conf_adv.item())
        drop_noise = abs(conf1.item() - conf2.item())
        entropy_increase = (entropy2 - entropy1).item()

        # -------------------------------
        # AUTOENCODER ERROR (OPTIONAL SIGNAL)
        # -------------------------------
        with torch.no_grad():
            recon = self.autoencoder(image)

        recon_error = torch.mean((image - recon) ** 2).item()

        # -------------------------------
        # FINAL RELAXED DECISION (KEY FIX ✅)
        # -------------------------------
        is_adv = False

        # VERY STRONG CONDITION → both unstable
        if (pred1.item() != pred_adv.item()) and (pred1.item() != pred2.item()):
            is_adv = True

        # STRONG CONDITION → big FGSM confidence drop
        elif drop_fgsm > 0.25:
            is_adv = True

        # OPTIONAL EXTRA (only for very strong anomalies)
        elif recon_error > 0.05:
            is_adv = True

        # -------------------------------
        # DEBUG OUTPUT
        # -------------------------------
        print("\n========== DEBUG ==========")
        print("Pred:", pred1.item(), "| Noise:", pred2.item(), "| FGSM:", pred_adv.item())
        print("Conf:", conf1.item(), "| FGSM:", conf_adv.item())
        print("Drop FGSM:", drop_fgsm)
        print("Drop Noise:", drop_noise)
        print("Entropy Increase:", entropy_increase)
        print("Recon Error:", recon_error)
        print("Final:", "ATTACK" if is_adv else "SAFE")
        print("===========================\n")

        # -------------------------------
        # RETURN
        # -------------------------------
        return {
            "is_adversarial": is_adv,
            "pred_before": pred1.item(),
            "pred_after": pred2.item(),
            "conf_before": conf1.item(),
            "conf_after": conf2.item(),
            "confidence_drop": drop_noise,
            "entropy_before": entropy1.item(),
            "entropy_after": entropy2.item(),
            "entropy_increase": entropy_increase,
            "reconstruction_error": recon_error
        }