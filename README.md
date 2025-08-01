# Deep Facial Diagnosis System 🧠📷

A web-based deep learning application that analyzes facial images to detect common skin conditions such as **acne**, **eczema**, **rosacea**, and identifies **healthy skin**. Built using **transfer learning** on VGG16 and deployed via a **Flask API**, the system aims to support early skin issue awareness.

---

## 🔍 Problem Statement

Skin conditions are often ignored until they become severe. This project automates early detection of common skin conditions from facial images using deep learning, improving awareness and promoting timely consultation.

---

## 🚀 Tech Stack

- **Deep Learning**: TensorFlow / Keras, Transfer Learning (VGG16)
- **Frontend**: HTML, CSS (basic UI)
- **Backend**: Flask (REST API)
- **Tools**: NumPy, OpenCV, Pillow, Matplotlib

---

## 👩‍💻 How It Works

1. **Input**: User uploads a facial image through the web interface.
2. **Processing**: The pre-trained VGG16 model classifies the image into one of the four categories.
3. **Output**: The predicted skin condition is displayed on the webpage.

---

## ⚙️ Features

- 🔁 **Transfer Learning**: Efficient use of VGG16 for robust feature extraction.
- 📸 **Image Classification**: Detects Acne, Eczema, Rosacea, or Healthy skin.
- 🌐 **Web Interface**: Simple UI to upload images and view results in real-time.

---

## 📂 Dataset

Due to the lack of publicly available datasets with clearly labeled facial skin conditions, a **custom dataset** was built. Images were collected from the web using `icrawler` and manually filtered into four classes:
- `acne`
- `eczema`
- `rosacea`
- `healthy`

> Each image was preprocessed (resized, normalized) and split into training and validation sets.

---

## 📊 Performance

- Validation Accuracy: ~84%
- Confusion matrix and detailed evaluation metrics included in training notebook.
- The model performs well on clear, frontal facial images.

---

## 🧩 Challenges Faced

- ⚠️ **Lack of Dataset**: Faced difficulties finding suitable medical-quality data. Solved by custom image scraping and manual labeling.
- 🧪 **Model Confusion**: Initially observed misclassifications. Improved via data augmentation and fine-tuning the base model.

---

## 📈 Results & Impact

- Successfully predicted conditions on custom and real-world facial images.
- Raised awareness on applying AI for healthcare screening.
- Demonstrated deployment of deep learning models on lightweight Flask applications.

---

## 🛠️ Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/DeepFacialDiagnosis.git
   cd DeepFacialDiagnosis


DeepFacialDiagnosis/
│
├── static/
│   └── uploaded_images/
├── templates/
│   └── index.html
├── app.py
├── best_model.h5
├── requirements.txt
└── README.md
