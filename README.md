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

- Model klasifikasi gender menggunakan regresi logistik.
- UI interaktif dengan Gradio untuk pengujian model secara langsung.
- Di-hosting di Hugging Face Spaces untuk akses publik.
- Manajemen data dan model menggunakan DVC.
- Monitoring data drift dengan Evidently, Prometheus, dan Grafana.
- Dikemas dalam Docker untuk portabilitas dan reproduktibilitas.
- Alur kerja CI/CD terintegrasi dengan GitHub Actions.

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
| **Discord**                    | Platform sebagai notifikasi alert                      |
| **MLflow**                     | Platform untuk melacak siklus hidup eksperimen ML      |
	

---

## 🧠 Gambaran Umum Model

- **Tipe Model**: Regresi Logistik
- **Tugas**: Prediksi gender
- **Input**: Fitur data terstruktur (Rambut Panjang, Lebar Dahi, Tinggi Dahi, Hidung Lebar, Hidung Panjang, Bibir Tipis)
- **Output**: Klasifikasi gender – Pria atau Wanita

---

## ♻️ Alur Kerja MLOps
- Proyek ini mengadopsi siklus MLOps yang terstruktur sebagai berikut:
- **1. Eksperimen: MLflow** digunakan untuk melacak setiap percobaan pelatihan model, termasuk parameter dan metrik performa, untuk memilih model terbaik.
- **2. Versioning: Git** digunakan untuk mengelola versi kode, sementara DVC digunakan untuk mengelola versi dataset dan file model yang besar agar repositori tetap ringan.
- **3. Packaging: Dockerfile** disiapkan untuk membungkus aplikasi, model, dan semua dependensinya ke dalam sebuah container yang portabel dan konsisten.
- **4. Deployment (CI/CD): Gradio** membangun antarmuka pengguna yang sederhana. Hugging Face Spaces secara otomatis men-deploy aplikasi dari repositori GitHub setiap kali ada perubahan pada branch utama.
- **5. Monitoring: Prometheus** mengumpulkan metrik ini secara berkala, dan Grafana memvisualisasikannya serta mengirimkan peringatan (alert) jika terdeteksi adanya masalah.

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
