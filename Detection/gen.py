import torch
import torch.nn as nn
from torchvision import datasets, transforms
import os
from models.classifier import load_model  # adjust if needed

# -------------------------------
# CONFIG
# -------------------------------
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
SAVE_DIR = "test_images"
os.makedirs(SAVE_DIR, exist_ok=True)

# -------------------------------
# LOAD MODEL
# -------------------------------
model = load_model("models/saved/cifar_model.pth", DEVICE)
model.eval()

# -------------------------------
# TRANSFORM (SAME AS TRAINING)
# -------------------------------
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,)*3, (0.5,)*3)
])

dataset = datasets.CIFAR10(root="./dataset", train=False, download=True, transform=transform)

# -------------------------------
# ATTACKS
# -------------------------------
criterion = nn.CrossEntropyLoss()

def fgsm_attack(image, label, eps=0.2):
    image = image.clone().detach().requires_grad_(True)

    output = model(image)
    loss = criterion(output, label)

    model.zero_grad()
    loss.backward()

    adv = image + eps * image.grad.sign()
    return torch.clamp(adv, -1, 1).detach()


def pgd_attack(image, label, eps=0.3, alpha=0.01, iters=5):
    ori = image.clone().detach()
    adv = ori.clone()

    for _ in range(iters):
        adv.requires_grad_(True)

        output = model(adv)
        loss = criterion(output, label)

        model.zero_grad()
        loss.backward()

        adv = adv + alpha * adv.grad.sign()
        eta = torch.clamp(adv - ori, -eps, eps)
        adv = torch.clamp(ori + eta, -1, 1).detach()

    return adv


# -------------------------------
# SAVE FUNCTION (DENORMALIZE)
# -------------------------------
def save_image(tensor, path):
    img = tensor.clone().cpu()
    img = img * 0.5 + 0.5  # denormalize
    img = torch.clamp(img, 0, 1)
    transforms.ToPILImage()(img.squeeze()).save(path)


# -------------------------------
# GENERATE IMAGES
# -------------------------------
count = 0

for i in range(len(dataset)):
    image, label = dataset[i]

    image = image.unsqueeze(0).to(DEVICE)
    label = torch.tensor([label]).to(DEVICE)

    # SAFE
    if count < 5:
        save_image(image, f"{SAVE_DIR}/safe_{count}.png")

    # FGSM
    if count < 5:
        adv_fgsm = fgsm_attack(image, label)
        save_image(adv_fgsm, f"{SAVE_DIR}/fgsm_{count}.png")

    # PGD
    if count < 5:
        adv_pgd = pgd_attack(image, label)
        save_image(adv_pgd, f"{SAVE_DIR}/pgd_{count}.png")

        count += 1

    if count >= 5:
        break

print("✅ 15 Images Generated Successfully!")
print("📂 Location: test_images/")