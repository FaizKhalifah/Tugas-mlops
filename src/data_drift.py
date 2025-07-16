import pandas as pd
import seaborn as sns
import mlflow
import matplotlib.pyplot as plt
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.evaluation.single_table import evaluate_quality
from sdv.evaluation.single_table import get_column_plot

try:
    df = pd.read_csv('../data/gender.csv')
    print("Dataset berhasil dimuat.")
except FileNotFoundError:
    print("Error: Pastikan file berada di direktori yang sama atau telah diunggah.")
    exit()

synthesizer = GaussianCopulaSynthesizer(df)
synthesizer.fit(data=df)
synthetic_data = synthesizer.sample(num_rows=500)