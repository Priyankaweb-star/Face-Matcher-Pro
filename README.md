# 🔍 Face Matcher Pro

Face Matcher Pro is an advanced Streamlit-based application that finds all occurrences of a person inside a large image dataset.
Upload 1 or more **reference face photos**, select a **dataset folder**, and the app scans every image, detects faces, compares them, and returns all matches with confidence scores.

---

## 🚀 Features

* 📁 **Scan Entire Dataset** — Point to any folder containing hundreds/thousands of images
* 🎭 **Multi-Face Detection** — Detects & compares all faces in an image
* 🧠 **AI-Powered Matching** — Uses `face_recognition` (dlib) with large/small models
* 🎚 Adjustable **Match Sensitivity**
* 🖼 Beautiful gallery of matched images with scores
* 📊 Stats dashboard (matches, scanned images, avg confidence)
* ⏬ Download ZIP of all matches
* 📝 Auto-generated TXT report
* ✨ Clean, modern UI with custom styling

---

## 🧠 How It Works

1. Upload 1–5 reference face images
2. The app extracts face encodings using:

   * `model="large"` (primary)
   * fallback: `model="small"`
3. It scans all images in the dataset folder
4. Detects all faces and calculates distances
5. Accepts matches using your threshold
6. Displays results with confidence scores
7. Allows exporting ZIP + report

---

## 📦 Tech Stack

* **Streamlit** — UI Framework
* **face_recognition** — Face detection + encodings
* **NumPy** — Distance calculations
* **Pillow (PIL)** — Image processing
* **zipfile / io** — Downloads

---

## 📁 Folder Structure

```
Face-Matcher-Pro/
│── app.py
│── requirements.txt
│── README.md
└── (your dataset folder – provided by user)
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/face-matcher-pro.git
cd face-matcher-pro
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

Your browser will open at:

```
http://localhost:8501
```

---

## 🎯 Usage Guide

### ✅ Step 1 — Enter Dataset Folder Path

Example:

```
C:/Users/Admin/Pictures/Dataset/
```

### ✅ Step 2 — Upload Reference Images

Upload clear frontal face photos.

### ✅ Step 3 — Adjust Settings

* Match Sensitivity
* Minimum Face Size
* Show/Hide Scores
* Sort by Score

### ✅ Step 4 — Click **Start Face Matching**

The system will:

* Process all images
* Detect faces
* Compare encodings
* Show matches in a grid

### ✅ Step 5 — Download Results

You can download:

* **ZIP file** containing all matched images
* **TXT report** (confidence, filenames, settings, stats)

---

## 📊 Output Example

* **Matches Found**: 22
* **Total Images Scanned**: 910
* **Average Confidence**: 91.4%
* **Threshold Used**: 0.48

---

## 🛠 Future Improvements

* Multi-person search (find multiple individuals at once)
* Automatic face clustering
* GPU acceleration
* Faster encoders (InsightFace, ArcFace)

---

