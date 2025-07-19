import pandas as pd
import seaborn as sns
import mlflow
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from skops import io as skops_io
import joblib

import matplotlib
matplotlib.use('Agg')  # non-GUI backend

  
# setup mlflow
mlflow.sklearn.autolog()
mlflow.set_tracking_uri("http://localhost:5000")


try:
    df = pd.read_csv('../data/combined_data.csv')
    print("Dataset berhasil dimuat.")
except FileNotFoundError:
    print("Error: Pastikan file berada di direktori yang sama atau telah diunggah.")
    exit()

df.head()

print("Contoh Data:")
print(df.head())
print("\nDistribusi Kelas:")
print(df['gender'].value_counts())

X = df.drop('gender', axis=1)
y = df['gender']

le = LabelEncoder()
y_encoded = le.fit_transform(y)
class_names = le.classes_

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print(f"Ukuran data latih: {X_train.shape}")
print(f"Ukuran data uji: {X_test.shape}")
print("-" * 35)

models = {
    "Logistic Regression": LogisticRegression(C=0.01), 
    "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=3), 
    "Gaussian Naive Bayes": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42)
}

results = []
mlflow.set_experiment("gender_classification")

for name, model in models.items():
    with mlflow.start_run(run_name=name.replace(" ", "_")):
        print(f"Melatih model {name}...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average="weighted")
        rec = recall_score(y_test, y_pred, average="weighted")
        f1 = f1_score(y_test, y_pred, average="weighted")

        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("precision", prec)
        mlflow.log_metric("recall", rec)
        mlflow.log_metric("f1_score", f1)

        mlflow.sklearn.log_model(model, artifact_path="model", registered_model_name=name.replace(" ", "_"))
        results.append([name, acc, prec, rec, f1])

        # 4. Save model
        model_path = f"../models/{name}.skops"
        skops_io.dump(model, model_path)
        print(f"Model {name} disimpan di {model_path}")

        # 5. Save confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(4, 3))
        sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=class_names, yticklabels=class_names)
        plt.title(f'Confusion Matrix - {name}')
        plt.xlabel("Predicted")
        plt.ylabel("True")
        plt.tight_layout()
        plt.savefig(f"../results/matrix/confusion_matrix_{name}.png")
        plt.close()

        image_path = f"../results/matrix/confusion_matrix_{name}.png"
        mlflow.log_artifact(image_path, artifact_path="confusion_matrices")

results_df = pd.DataFrame(results, columns=["Model", "Accuracy", "Precision", "Recall", "F1-Score"])
results_df.to_csv("../results/csv/evaluation_metrics.csv", index=False)
print("Evaluasi disimpan di results/csv/evaluation_metrics.csv")

# plt.tight_layout(rect=[0, 0, 1, 0.95])
# plt.show()