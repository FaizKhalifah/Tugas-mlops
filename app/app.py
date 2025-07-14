import gradio as gr
import pandas as pd
from skops import io as skops_io
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

modelname = "Logistic Regression.skops"

# Coba path di HF (semua di root folder)
path1 = os.path.join("models", modelname)

# Coba path di lokal (struktur: app/app.py, models/...)
path2 = os.path.join("..", "models", modelname)

# Pilih path yang ada
if os.path.exists(path1):
    model_path = path1
elif os.path.exists(path2):
    model_path = path2
else:
    raise FileNotFoundError("Model tidak ditemukan di path yang dicoba.")
# Load model
model = skops_io.load(model_path)

# Coba ambil label encoder dari model jika ada attribute classes_
if hasattr(model, 'classes_'):
    label_classes = list(model.classes_)
    # Asumsi label_classes berisi ['Female', 'Male'] atau sebaliknya
    label_map = {i: label for i, label in enumerate(label_classes)}
else:
    # Fallback ke mapping default
    label_map = {0: "Female", 1: "Male"}

# Fungsi prediksi dengan error handling

def predict_gender(long_hair, forehead_width_cm, forehead_height_cm, nose_wide,
                   nose_long, lips_thin, distance_nose_to_lip_long):
    try:
        input_df = pd.DataFrame([{
            "long_hair": int(long_hair),
            "forehead_width_cm": float(forehead_width_cm),
            "forehead_height_cm": float(forehead_height_cm),
            "nose_wide": int(nose_wide),
            "nose_long": int(nose_long),
            "lips_thin": int(lips_thin),
            "distance_nose_to_lip_long": int(distance_nose_to_lip_long),
        }])
        pred = model.predict(input_df)[0]
        return label_map.get(pred, str(pred))
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio UI
interface = gr.Interface(
    fn=predict_gender,
    inputs=[
        gr.Radio(["0", "1"], label="Long Hair (1 = Yes, 0 = No)"),
        gr.Number(label="Forehead Width (cm)"),
        gr.Number(label="Forehead Height (cm)"),
        gr.Radio(["0", "1"], label="Nose Wide (1 = Yes, 0 = No)"),
        gr.Radio(["0", "1"], label="Nose Long (1 = Yes, 0 = No)"),
        gr.Radio(["0", "1"], label="Lips Thin (1 = Yes, 0 = No)"),
        gr.Radio(["0", "1"], label="Distance Nose to Lip Long (1 = Yes, 0 = No)")
    ],
    outputs="text",
    title="Gender Classification",
    description="Masukkan ciri-ciri wajah untuk memprediksi gender.",
)

if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=7860)
