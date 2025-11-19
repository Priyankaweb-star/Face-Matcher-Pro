import streamlit as st
import face_recognition
import numpy as np
import os
import zipfile
from PIL import Image

st.set_page_config(page_title="Face Matcher", layout="wide")
st.title("🔍 Face Matcher - Upload & Find Matches")

# Ask user for dataset folder
dataset_folder = st.text_input(
    "📂 Enter the folder path containing images to search in:",
    placeholder="Example: C:/Priyanka1/face-matcher-project/data/Faces/Faces/"
)

uploaded_files = st.file_uploader(
    "Upload 1 or more images of the same person",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

# Validate folder
if dataset_folder:
    if not os.path.exists(dataset_folder):
        st.error("❌ Folder does not exist. Please enter a valid path.")
    else:
        st.success("✅ Folder loaded successfully!")

# If uploaded images exist
if uploaded_files and dataset_folder and os.path.exists(dataset_folder):

    st.subheader("Uploaded Images")
    cols = st.columns(3)

    uploaded_encodings = []

    # Encode uploaded images
    for idx, file in enumerate(uploaded_files):
        img = face_recognition.load_image_file(file)
        enc = face_recognition.face_encodings(img)

        if enc:
            uploaded_encodings.append(enc[0])
            cols[idx % 3].image(img, caption=f"Uploaded #{idx+1}")
        else:
            st.error(f"No face detected in {file.name}")

    if len(uploaded_encodings) == 0:
        st.warning("❗ No valid faces found in uploaded images.")
        st.stop()

    st.info("✔ Images loaded. Click 'Start Matching' to find similar faces.")

    if st.button("Start Matching"):

        st.subheader("Matching Results")

        matched_images = []
        scores = []

        all_images = [
            img for img in os.listdir(dataset_folder)
            if img.lower().endswith((".jpg", ".jpeg", ".png"))
        ]

        progress = st.progress(0)

        for i, img_name in enumerate(all_images):

            path = os.path.join(dataset_folder, img_name)

            try:
                db_img = face_recognition.load_image_file(path)
                db_enc = face_recognition.face_encodings(db_img)

                if not db_enc:
                    continue  # skip images without face

                db_enc = db_enc[0]

                # Compare with ALL uploaded images
                distances = face_recognition.face_distance(uploaded_encodings, db_enc)
                best_score = 1 - np.min(distances)

                if np.min(distances) < 0.45:  # tuned threshold
                    matched_images.append(path)
                    scores.append(best_score)

            except:
                continue

            progress.progress((i + 1) / len(all_images))

        if len(matched_images) == 0:
            st.warning("❌ No matches found.")
        else:
            st.success(f"🎉 Found {len(matched_images)} Matches")

            # Show result grid
            result_cols = st.columns(4)
            for idx, path in enumerate(matched_images):
                img = Image.open(path)
                result_cols[idx % 4].image(
                    img,
                    caption=f"{os.path.basename(path)}\nScore: {scores[idx]:.2f}"
                )

            # Download ZIP
            zip_path = "matched_results.zip"
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for p in matched_images:
                    zipf.write(p, os.path.basename(p))

            with open(zip_path, "rb") as f:
                st.download_button(
                    "⬇ Download All Matched Images",
                    f,
                    file_name="matched_images.zip"
                )
