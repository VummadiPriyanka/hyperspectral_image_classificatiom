# 🌈 Hyperspectral Image Classification using Deep Learning

This project uses Convolutional Neural Networks (CNNs) to classify hyperspectral image data — enabling pixel-wise classification of materials or land types from rich spectral data. Built as part of an academic AIML project to demonstrate real-world applications of AI in remote sensing.

---

## 🔗 Live App
👉 [Streamlit App](https://your-app-link.streamlit.app/) *(replace with your live link)*

---

## 📌 Problem Statement

Hyperspectral images capture hundreds of narrow spectral bands, making them ideal for applications in agriculture, mineralogy, and surveillance. However, classifying such high-dimensional data requires advanced deep learning techniques to avoid overfitting and extract relevant features.

---

## 🛰️ Dataset

- **Source**: [Indian Pines / Pavia University / Salinas Scene – Hyperspectral datasets]
- **Bands**: Up to 200+ spectral bands per pixel
- **Preprocessing**:
  - Dimensionality reduction (e.g., PCA)
  - Normalization & resizing
  - Ground truth labels for classification

---

## 🧠 Model Architecture

- **Model**: Convolutional Neural Network (CNN)
- **Layers**:
  - Convolution → ReLU → MaxPooling
  - Fully Connected → Softmax
- **Loss Function**: Categorical Crossentropy
- **Optimizer**: Adam
- **Accuracy Achieved**: *Mention test accuracy here*

---

## 🖥️ Technologies Used

- `Python`, `NumPy`, `Pandas`
- `TensorFlow`, `Keras`
- `Matplotlib`, `Seaborn`
- `Streamlit` – For interactive demo

---

## 📦 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/VummadiPriyanka/hyperspectral_classifier.git
cd hyperspectral_classifier

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py
