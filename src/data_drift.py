import pandas as pd
import seaborn as sns
import mlflow
import matplotlib.pyplot as plt


from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata
import pandas as pd

try:
    data = pd.read_csv('../data/gender.csv')
    print("Dataset berhasil dimuat.")
except FileNotFoundError:
    print("Error: Pastikan file berada di direktori yang sama atau telah diunggah.")
    exit()

metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data)

model = GaussianCopulaSynthesizer(metadata)
model.fit(data)
synthetic = model.sample(num_rows=len(data))

# save synthetic data
synthetic.to_csv('../data/synthetic_data.csv', index=False)

#save combined data
combined = pd.concat([data, synthetic], ignore_index=True)
combined.to_csv("../data/combined_data.csv", index=False)