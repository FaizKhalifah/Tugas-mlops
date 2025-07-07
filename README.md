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

## 💡 Features

- Gender classification model using logistic regression
- Interactive UI with Gradio
- Hosted on Hugging Face Spaces
- Secret token management for deployment
- Ready for CI/CD and version control integration

---

## ⚙️ Tech Stack

- **Python**
- **Scikit-learn** – model training
- **Gradio** – frontend interface
- **Hugging Face Spaces** – model hosting
- **DVC (optional)** – versioning data and models
- **GitHub Actions (optional)** – automation for CI/CD

---

## 🧠 Model Overview

- **Model Type**: Logistic Regression
- **Task**: Gender prediction
- **Input**: Structured data features (e.g., height, weight, etc.)
- **Output**: Gender classification – Male or Female

---
