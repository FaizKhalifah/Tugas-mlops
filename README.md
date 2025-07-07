---
title: Tugasmlops
emoji: 🌍
colorFrom: indigo
colorTo: indigo
sdk: gradio
sdk_version: 5.35.0
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# 📌 Tugas MLOps

This is a project for the **Machine Learning Operations (MLOps)** course. It demonstrates the use of a complete MLOps workflow—from model development to deployment—using a **gender classification dataset**.

The model used is **Logistic Regression**, and it is deployed using **Gradio** for the user interface and **Hugging Face Spaces** for production hosting.

---

## 📊 Dataset

- **Nama**: `gender.csv`  
- **Tipe**: CSV (Comma Separated Values)  
- **Deskripsi**: Dataset ini digunakan untuk mengklasifikasikan jenis kelamin berdasarkan fitur wajah.  
- **Tautan**: [Kaggle Dataset](https://www.kaggle.com/datasets/elakiricoder/gender-classification-dataset)

---

## 💡 Features

- Gender classification model using logistic regression
- Interactive UI with Gradio
- Hosted on Hugging Face Spaces
- Secret token management for deployment
- Ready for CI/CD and version control integration

---

## 🧠 Algoritma Model

- **Model**: Gaussian Naive Bayes  
- **Alasan Pemilihan**:
  - Sangat cocok untuk fitur numerik atau kontinu seperti `forehead_width_cm` dan `forehead_height_cm`.
  - Mengasumsikan distribusi Gaussian pada fitur untuk tiap kelas (Pria/Wanita).
  - Efisien dalam perhitungan probabilitas.
  - Cepat dalam pelatihan dan prediksi.
  - Efektif meskipun data pelatihan terbatas.

---

## ⚙️ Tech Stack

| Tools              | Deskripsi                                      |
|-------------------|-----------------------------------------------|
| **Python**         | Bahasa pemrograman utama                      |
| **Scikit-learn**   | Library untuk model GaussianNB                |
| **Gradio**         | UI interaktif berbasis Python                 |
| **Hugging Face Spaces** | Platform hosting dan deployment          |
| **GitHub**         | Repositori kode dan pengaturan CI/CD          |
| **Google Colab**   | Tempat eksplorasi dan pelatihan model awal    |
| **Docker**   | Tempat eksplorasi dan pelatihan model awal    |

---

## 🧠 Model Overview

- **Model Type**: Logistic Regression
- **Task**: Gender prediction
- **Input**: Structured data features (Long Hair, Forehead Width, Forehead Height, Nose Wide, Nose Long, Lips Thin)
- **Output**: Gender classification – Male or Female

---

## 👥 Tim & Kontribusi

| Nama Lengkap                             | NIM              |
|------------------------------------------|------------------|
| Raihan Fadhillah Baihaqi                 | 225150207111069  |
| Hernando Atha                            | 225150207111075  |
| Muhammad Alfaiz Khalifah Alamsyah        | 225150207111066  |
| Qyan Rommy Mario                         | 225150200111034  |
| Davin Dalana Fidelio Fredra              | 225150201111029  |

---

## 🏫 Institusi

- **Program Studi**: Teknik Informatika  
- **Departemen**: Teknik Informatika  
- **Fakultas**: Ilmu Komputer  
- **Universitas**: Universitas Brawijaya – Malang  
- **Tahun**: 2025

---
