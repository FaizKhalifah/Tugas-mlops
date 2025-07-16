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

Cek referensi konfigurasi di https://huggingface.co/docs/hub/spaces-config-reference

# 📌 Tugas MLOps

Ini adalah proyek untuk mata kuliah **Machine Learning Operations (MLOps)**. Proyek ini mendemonstrasikan penggunaan alur kerja MLOps yang lengkap—mulai dari pengembangan model hingga deployment—menggunakan **dataset klasifikasi gender**.

Model yang digunakan adalah **Regresi Logistik**, dan di-deploy menggunakan **Gradio** untuk antarmuka pengguna serta **Hugging Face Spaces** untuk hosting produksi.

---

## 📊 Dataset

- **Nama**: `gender.csv`
- **Tipe**: CSV (Comma Separated Values)
- **Deskripsi**: Dataset ini digunakan untuk mengklasifikasikan jenis kelamin berdasarkan fitur wajah.
- **Tautan**: [Kaggle Dataset](https://www.kaggle.com/datasets/elakiricoder/gender-classification-dataset)

---

## 💡 Fitur

- Model klasifikasi gender menggunakan regresi logistik
- UI interaktif dengan Gradio
- Di-hosting di Hugging Face Spaces
- Manajemen token rahasia untuk deployment
- Siap untuk integrasi CI/CD dan kontrol versi

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

## ⚙️ Tumpukan Teknologi

| Tools                          | Deskripsi                                              |
| ------------------------------ | ------------------------------------------------------ |
| **Python**                     | Bahasa pemrograman utama                               |
| **Scikit-learn**               | Library untuk model GaussianNB                         |
| **Gradio**                     | UI interaktif berbasis Python                          |
| **Hugging Face Spaces**        | Platform hosting dan deployment                        |
| **GitHub**                     | Repositori kode dan pengaturan CI/CD                   |
| **Google Colab**               | Tempat eksplorasi dan pelatihan model awal             |
| **Docker**                     | Platform untuk mengemas aplikasi dan dependensi        |
| **Prometheus**                 | Sistem pemantauan dan peringatan sumber terbuka        |
| **Grafana**                    | Platform analitik dan visualisasi untuk metrik         |
| **DVC (Data Version Control)** | Sistem kontrol versi untuk data dan model              |
| **SDV (Synthetic Data Vault)** | Library untuk membuat data sintetis berkualitas tinggi |

---

## 🧠 Gambaran Umum Model

- **Tipe Model**: Regresi Logistik
- **Tugas**: Prediksi gender
- **Input**: Fitur data terstruktur (Rambut Panjang, Lebar Dahi, Tinggi Dahi, Hidung Lebar, Hidung Panjang, Bibir Tipis)
- **Output**: Klasifikasi gender – Pria atau Wanita

---

## 👥 Tim & Kontribusi

| Nama Lengkap                      | NIM             |
| --------------------------------- | --------------- |
| Raihan Fadhillah Baihaqi          | 225150207111069 |
| Hernando Atha                     | 225150207111075 |
| Muhammad Alfaiz Khalifah Alamsyah | 225150207111066 |
| Qyan Rommy Mario                  | 225150200111034 |
| Davin Dalana Fidelio Fredra       | 225150201111029 |

---

## 🏫 Institusi

- **Program Studi**: Teknik Informatika
- **Departemen**: Teknik Informatika
- **Fakultas**: Ilmu Komputer
- **Universitas**: Universitas Brawijaya – Malang
- **Tahun**: 2025
