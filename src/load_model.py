from skops import io as skops_io
import pandas as pd

# Load model
model_path = "models/LogisticRegression.skops"
model = skops_io.load(model_path)

# Contoh input (bisa ganti dengan data baru atau X_test)
data = pd.read_csv("data/gender.csv").drop("gender", axis=1)
sample = data.iloc[[0]]  # ambil satu baris

# Prediksi
prediction = model.predict(sample)
print("Prediksi:", prediction)
