# 🚀 Adversarial Attack Detection with Blockchain Audit Trails

## 📌 Project Overview

This project presents an AI-powered adversarial attack detection framework integrated with blockchain-based audit trails for secure and trustworthy deep learning systems.

The system is designed to detect adversarially manipulated images using deep learning, entropy analysis, confidence score monitoring, Gaussian noise perturbation, and autoencoder-based reconstruction analysis. Detected attacks are securely logged using Blockchain and IPFS technologies to ensure immutability, transparency, and tamper-proof security.

---

# 🔥 Key Features

✅ Adversarial Attack Detection  
✅ FGSM & PGD Attack Simulation  
✅ ResNet-based Image Classification  
✅ Confidence Score Monitoring  
✅ Entropy-based Detection  
✅ Autoencoder Reconstruction Analysis  
✅ Gaussian Noise Stability Testing  
✅ Blockchain-based Secure Logging  
✅ IPFS Decentralized Storage  
✅ Ethereum Smart Contract Integration  
✅ Tamper-proof Audit Trails  
✅ CIFAR-10 Dataset Support

---

# 🧠 Technologies Used

| Technology         | Purpose               |
| ------------------ | --------------------- |
| Python             | Core Development      |
| TensorFlow / Keras | Deep Learning         |
| ResNet             | Image Classification  |
| CNN                | Feature Extraction    |
| OpenCV             | Image Processing      |
| NumPy              | Numerical Operations  |
| Matplotlib         | Visualization         |
| Flask              | Web Application       |
| Blockchain         | Secure Logging        |
| Ethereum           | Smart Contracts       |
| IPFS               | Decentralized Storage |

---

# 🏗️ System Architecture

The proposed system integrates deep learning with blockchain security mechanisms.

## Workflow:

1. Input Image Upload
2. Image Classification using ResNet
3. Adversarial Attack Generation (FGSM/PGD)
4. Detection using:
   - Confidence Drop
   - Entropy Analysis
   - Noise Stability
   - Autoencoder Reconstruction Error
5. Risk Analysis
6. Blockchain Hash Generation
7. IPFS Secure Storage
8. Blockchain Audit Logging

---

# 🧪 Adversarial Attacks Used

## 🔹 FGSM (Fast Gradient Sign Method)

FGSM creates adversarial examples using gradient-based perturbations.

### Formula

\[
x\_{adv} = x + \epsilon \cdot sign(\nabla_x L(\theta, x, y))
\]

---

## 🔹 PGD (Projected Gradient Descent)

PGD performs iterative adversarial perturbation.

### Formula

\[
x^{t+1} = Clip\_{x,\epsilon}
(x^t + \alpha \cdot sign(\nabla_x L(\theta, x^t, y)))
\]

---

# 🧠 Deep Learning Model

The project uses:

## ✅ ResNet Architecture

ResNet improves training stability using residual skip connections.

### Residual Learning Formula

\[
F(x) = H(x) - x
\]

\[
y = F(x) + x
\]

---

# 🔍 Detection Mechanism

The system identifies adversarial inputs using multiple robustness metrics:

## ✅ Confidence Score Analysis

\[
Confidence = max(\hat{y_k})
\]

---

## ✅ Entropy Analysis

\[
H(p) = -\sum p_k log(p_k)
\]

---

## ✅ Reconstruction Error

\[
Error = \frac{1}{n} \sum (x - \hat{x})^2
\]

---

# 🔐 Blockchain Integration

The project integrates Blockchain + IPFS for secure adversarial logging.

## Security Workflow

Detection → Hash Generation → IPFS Storage → Blockchain Logging

---

# 🌐 IPFS Integration

IPFS stores adversarial data securely using content-based addressing.

## CID Generation

\[
CID = Encode(Hash(D))
\]

---

# 📊 Results & Performance Analysis

The proposed system demonstrates:

✅ High adversarial detection accuracy  
✅ Robustness against FGSM & PGD attacks  
✅ Stable confidence analysis  
✅ Improved detection using Gaussian noise  
✅ Secure immutable blockchain logging

---

# 📈 Evaluation Metrics

The following metrics are used:

- Accuracy
- Precision
- Recall
- F1-Score
- Entropy Change
- Confidence Drop
- Reconstruction Error

---

# 📷 Project Screenshots

## Home Interface

(Add screenshot here)

## Detection Results

(Add screenshot here)

## Blockchain Logs

(Add screenshot here)

## Accuracy Graphs

(Add screenshot here)

---

# 🔮 Future Scope

- Real-time attack monitoring
- Federated learning integration
- Advanced adversarial defenses
- Explainable AI integration
- Cloud-based deployment
- Hybrid blockchain optimization

---

# 🎯 Conclusion

This project successfully combines Artificial Intelligence and Blockchain technologies to create a secure and trustworthy adversarial attack detection framework.

The integration of deep learning robustness techniques with decentralized audit trails improves transparency, security, and reliability in AI systems.

---

# 👩‍💻 Author

## Shivani Chauhan

Final Year B.Tech Project  
Computer Science & Engineering

---

# ⭐ Repository Highlights

✅ Deep Learning  
✅ Cybersecurity  
✅ Adversarial Machine Learning  
✅ Blockchain Security  
✅ Research-Based Project  
✅ AI Robustness Framework

---

# 📚 References

- CIFAR-10 Dataset
- TensorFlow Documentation
- Ethereum Documentation
- IPFS Documentation
- ResNet Research Paper
- FGSM & PGD Adversarial Attack Papers

# 📊 Results and Performance Analysis

The proposed adversarial attack detection framework was evaluated using multiple robustness, classification, and security metrics. The results demonstrate strong detection capability, improved robustness against adversarial attacks, and secure blockchain-based audit logging.

---

# 🔹 Training Performance Analysis

## Training vs Validation Accuracy

![Training vs Validation Accuracy](images/Training%20vs%20Validation%20Accuracy.png)

### Analysis

The graph shows stable convergence of both training and validation accuracy, indicating reduced overfitting and strong generalization performance of the proposed deep learning model.

---

## Training Loss vs Epochs

![Training Loss](images/Training%20Loss%20vs%20Epochs.png)

### Analysis

Training loss decreases consistently with epochs, demonstrating effective optimization and stable learning behavior.

---

## Training vs Validation Loss

![Training vs Validation Loss](images/Training%20vs%20Validation%20Loss.png)

### Analysis

The validation loss remains close to training loss, showing strong model stability and robustness.

---

# 🔹 Adversarial Robustness Analysis

## Accuracy vs Perturbation Level

![Accuracy vs Perturbation](images/Accuracy%20vs%20Perturbation%20level.png)

### Analysis

The graph demonstrates how model accuracy changes under different perturbation strengths. Accuracy gradually decreases as perturbation increases, validating adversarial sensitivity.

---

## Detection Accuracy

![Detection Accuracy](images/Detection%20Accuracy.png)

### Analysis

The proposed detection framework achieves high adversarial detection accuracy against FGSM and PGD attacks.

---

## Model Accuracy Before vs After Attack

![Model Accuracy Before vs After Attack](images/Model%20Accuracy%20Before%20vs%20After%20Attack.png)

### Analysis

The graph compares model performance before and after adversarial attacks, highlighting the effectiveness of the proposed defense mechanism.

---

# 🔹 Classification Metrics

## Precision, Recall and F1-Score Analysis

![Precision Recall F1](images/Precision,Recall,F-1%20score%20analysis.png)

### Analysis

The model demonstrates high precision, recall, and F1-score values, indicating strong classification capability.

---

## Precision, Recall and F1-Score Comparison

![Precision Recall F1 2](images/Precision%20,Recall,F-1%20score2.png)

### Analysis

The comparison graph validates balanced classification performance across multiple classes.

---

## Classwise Accuracy Analysis

![Classwise Accuracy](images/Classwise%20Accuracy%20Analysis.png)

### Analysis

The model achieves consistent performance across different classes, showing strong feature extraction capability.

---

## Confusion Matrix

![Confusion Matrix](images/Confusion%20matrix.png)

### Analysis

The confusion matrix demonstrates accurate classification with minimal misclassification errors.

---

# 🔹 System Dashboard and Prediction Results

## System Dashboard

![Dashboard](images/Dashboard%20image.png)

### Analysis

The dashboard provides real-time visualization of adversarial detection, prediction confidence, and blockchain logging activities.

---

## Safe Image Prediction

![Safe Prediction](images/Safe%20image%20prediction1.png)

### Analysis

The system correctly identifies normal images with high confidence and low risk scores.

---

## Low Risk Image Predictions

![Low Risk Prediction 1](images/Low%20risk%20image%20prediction1.png)

![Low Risk Prediction 2](images/Low%20risk%20image%20prediction2.png)

### Analysis

Low-risk predictions indicate slight perturbations with limited impact on classification stability.

---

## High Risk Image Predictions

![High Risk Prediction 1](images/High%20risk%20image%20prediction1.png)

![High Risk Prediction 2](images/High%20risk%20image%20prediction2.png)

![High Risk Prediction 3](images/High%20risk%20image%20prediction3.png)

### Analysis

The proposed framework successfully detects highly adversarial inputs using entropy, confidence drop, and reconstruction error analysis.

---

# 🔹 Blockchain Security Analysis

## Blockchain Performance

![Blockchain Performance](images/Blockchain%20Performance.png)

### Analysis

Blockchain integration ensures secure, tamper-proof, and transparent storage of adversarial detection logs.

---

# 📈 Final Performance Summary

| Metric                         | Result                      |
| ------------------------------ | --------------------------- |
| Clean Accuracy                 | High                        |
| Adversarial Detection Accuracy | Excellent                   |
| Precision                      | High                        |
| Recall                         | High                        |
| F1-Score                       | Strong                      |
| Security                       | Blockchain Verified         |
| Robustness                     | Improved Against FGSM & PGD |
| Stability                      | High                        |

---

# 🎯 Overall Outcome

The proposed system successfully integrates Artificial Intelligence, Adversarial Machine Learning, and Blockchain Technology to build a secure and trustworthy adversarial attack detection framework capable of detecting manipulated inputs while maintaining secure audit trails.
