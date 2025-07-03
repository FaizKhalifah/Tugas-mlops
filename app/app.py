import gradio as gr
import pandas as pd
from skops import io as skops_io

# Load model
model_path = "../models/Logistic Regression.skops"  # bisa diganti model lain
model = skops_io.load(model_path)

# Label encoder (0 = Female, 1 = Male) → disesuaikan dari hasil training
label_map = {0: "Female", 1: "Male"}

# Fungsi prediksi
def predict_gender(long_hair, forehead_width_cm, forehead_height_cm, nose_wide,
                   nose_long, lips_thin, distance_nose_to_lip_long):
    
    input_df = pd.DataFrame([{
        "long_hair": int(long_hair),
        "forehead_width_cm": forehead_width_cm,
        "forehead_height_cm": forehead_height_cm,
        "nose_wide": int(nose_wide),
        "nose_long": int(nose_long),
        "lips_thin": int(lips_thin),
        "distance_nose_to_lip_long": int(distance_nose_to_lip_long),
    }])

    pred = model.predict(input_df)[0]
    return label_map.get(pred, "Unknown")

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
    interface.launch()
