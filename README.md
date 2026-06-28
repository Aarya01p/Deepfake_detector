# 🛡️ Deepfake Detection Using EfficientNetB0

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Gradio](https://img.shields.io/badge/Gradio-Web%20App-blueviolet.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A deep learning-based image classification system that detects whether a facial image is **Real** or **AI-generated (Deepfake)** using **EfficientNetB0** and **TensorFlow**. The project includes a trained model, evaluation metrics, and a user-friendly Gradio web interface for real-time predictions.

---

# 📌 Project Overview

Deepfakes have become increasingly realistic with the advancement of Generative AI, creating serious concerns in digital security, misinformation, identity theft, and online fraud.

This project uses transfer learning with EfficientNetB0 to classify facial images as real or AI-generated. The model is trained on a balanced dataset of over 140,000 images and deployed through a Gradio web interface for real-time inference.

The model is trained on a balanced dataset containing over **140,000 facial images**, consisting of both real and AI-generated images.

---
## 🖼️ Application Preview

Below is the Gradio interface of the Deepfake Detection application:

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/07edf157-2d2b-4f2a-b199-66a2cd41c783" />


---
## ⚙️ How It Works

The detection pipeline follows these steps:

```text
Input Image
      │
      ▼
Resize to 224 × 224
      │
      ▼
Data Augmentation
      │
      ▼
EfficientNetB0 Feature Extraction
      │
      ▼
Global Average Pooling
      │
      ▼
Dense Layers
      │
      ▼
Sigmoid Output Layer
      │
      ▼
Prediction (Real / Fake)
```

The model uses transfer learning with EfficientNetB0 to extract facial features and classify an uploaded image as either **Real** or **Fake**.

---

# ✨ Features

- Detects Real vs Fake facial images
- Transfer Learning using EfficientNetB0
- TensorFlow Data Pipeline
- Real-time predictions with Gradio
- Data augmentation for better generalization
- Early Stopping
- Learning Rate Scheduling
- Model Checkpointing
- Binary Classification
- GPU accelerated training
- Ready for deployment on Hugging Face Spaces

---

# 🏗️ Project Structure

```
Deepfake-Detection/

│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── assets/
│   └── sample_images/
       ├── fake-sample.png
       └── real-sample.png
    └── ReadMe.md
│
├── images/
│   ├── confusion_matrix.png
│   ├── interface.png
│   └── roc_curve.png
│
├── notebooks/
│   └── Deepfake_Detection.ipynb
│
└── results/
    ├── classification_report.txt
    └── metrics.txt
```

---

# 🧠 Model Architecture

```
Input Image (224×224×3)

        │

Image Preprocessing

        │

Data Augmentation

        │

EfficientNetB0 (ImageNet Weights)

        │

Global Average Pooling

        │

Dense (256) + ReLU

        │

Dropout (0.5)

        │

Dense (128) + ReLU

        │

Dropout (0.3)

        │

Dense (1)

        │

Sigmoid

        │

Prediction
```

---

# 📂 Dataset

The dataset consists of facial images divided into two classes:

```
Dataset/

├── Real/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
│
└── Fake/
    ├── image1.jpg
    ├── image2.jpg
    └── ...
```

### Dataset Statistics

| Class | Images |
|--------|--------|
| Real | 70,001 |
| Fake | 70,001 |
| Total | **140,002** |

> **Note:** The complete dataset is not included in this repository due to its large size (140,002 images).

---

# ⚙️ Data Preprocessing

The following preprocessing pipeline is used:

- Image resizing (224 × 224)
- EfficientNet preprocessing
- Batch loading using `tf.data`
- Automatic shuffling
- Prefetching
- Data augmentation

### Data Augmentation

- Horizontal Flip
- Random Rotation
- Random Zoom

---

# 🚀 Training Configuration

| Parameter | Value |
|------------|--------|
| Image Size | 224 × 224 |
| Batch Size | 32 |
| Optimizer | Adam |
| Learning Rate | 1e-4 |
| Loss Function | Binary Crossentropy |
| Epochs | 10 |
| Transfer Learning | EfficientNetB0 |

### Callbacks

- EarlyStopping
- ReduceLROnPlateau
- ModelCheckpoint

---

# 📊 Evaluation Metrics

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix
- Validation Loss

---
## 📊 Model Performance

The trained model achieved the following performance on the validation dataset:

| Metric | Score |
|---------|------:|
| Accuracy | **86%** |
| Precision | **88%** |
| Recall | **86%** |
| F1 Score | **86%** |
| Validation Images | **28,000** |

### Classification Report

| Class | Precision | Recall | F1-Score |
|-------|----------:|-------:|---------:|
| Real | 0.80 | 0.96 | 0.87 |
| Fake | 0.95 | 0.76 | 0.85 |

---

# 🖥️ Gradio Interface

The application provides an easy-to-use interface where users can:

- Upload an image
- Predict Real or Fake
- View confidence scores
- Receive probability distribution

Example Output:

```
Prediction

✅ REAL

Confidence

Real : 97%

Fake : 3%
```

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/Aarya01p/deepfake-detection.git

cd deepfake-detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Live Demo

Try the deployed application here:

```
https://aarya47-deepfake-detector.hf.space/
```

---

# 📦 Requirements

- Python 3.10+
- TensorFlow
- NumPy
- Pillow
- OpenCV
- Gradio

---

# 📈 Future Improvements

- Face Detection (MTCNN)
- Fine-tuning EfficientNetB0
- Video Deepfake Detection
- Explainable AI with Grad-CAM
- Mobile Deployment

---

# 📚 Technologies Used

- Python
- TensorFlow
- Keras
- EfficientNetB0
- OpenCV
- NumPy
- Gradio
- Matplotlib
- Scikit-Learn

---

# 🎯 Applications

- Fake News Detection
- Social Media Verification
- Digital Forensics
- Identity Protection
- Content Moderation
- Media Authentication

---

# 👨‍💻 Author

**Aarya Patel**

Computer Science Student

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Acknowledgements

- TensorFlow
- Keras
- EfficientNet
- Gradio
- Kaggle
- Hugging Face



## 📬 Contact

If you found this project useful, consider giving it a ⭐ on GitHub.

For suggestions or improvements, feel free to open an issue or submit a pull request.


**Built with TensorFlow, EfficientNetB0, and Gradio to explore practical AI solutions for deepfake image detection.**
