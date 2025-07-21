from flask import Flask, Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import start_http_server
import pandas as pd
import numpy as np

app = Flask(__name__)

# Metrik utama
drift_detected = Gauge('data_drift_detected', 'Data drift detected (1 = yes, 0 = no)')

# Metrik per fitur
features = ['forehead_width_cm',
    'forehead_height_cm',
    'nose_wide',
    'nose_long',
    'lips_thin',
    'distance_nose_to_lip_long']  # ganti sesuai fitur datamu
feature_means_ref = {}
feature_means_current = {}
feature_drift = {}

# Prometheus Gauge per fitur
drift_per_feature = {
    feature: Gauge(f'drift_detected_{feature}', f'Drift detected for {feature}') for feature in features
}

# Load reference data
reference_data = pd.read_csv('../data/gender.csv')
reference_means = reference_data[features].mean()

@app.route('/metrics')
def metrics():
    current_data = pd.read_csv('../data/combined_data.csv')
    current_means = current_data[features].mean()

    drift_flag = False

    for feature in features:
        mean_ref = reference_means[feature]
        mean_current = current_means[feature]

        # Deteksi drift jika perubahan > 20% (bisa diatur sesuai kebutuhan)
        if mean_ref == 0:
            drift = abs(mean_current) > 0.1
        else:
            drift = abs(mean_current - mean_ref) / abs(mean_ref) > 0.2

        drift_per_feature[feature].set(1 if drift else 0)

        if drift:
            drift_flag = True

    drift_detected.set(1 if drift_flag else 0)

    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    start_http_server(8000)  # opsional jika tidak pakai Flask
    app.run(host='0.0.0.0', port=5002)
