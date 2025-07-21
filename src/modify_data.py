import pandas as pd
import numpy as np

# Load original data
df = pd.read_csv("../data/gender.csv")

# Simulasi perubahan distribusi numerik
df['forehead_width_cm'] = np.random.normal(loc=30, scale=5, size=len(df))        # beda jauh
df['forehead_height_cm'] = np.random.normal(loc=20, scale=5, size=len(df))

# Simulasi biner jadi sebaliknya (flip)
df['nose_wide'] = 1 - df['nose_wide']
df['nose_long'] = 1 - df['nose_long']
df['lips_thin'] = 1 - df['lips_thin']
df['distance_nose_to_lip_long'] = 1 - df['distance_nose_to_lip_long']

# Simpan ulang sebagai current data
df.to_csv("../data/combined_data.csv", index=False)
