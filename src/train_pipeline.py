import pandas as pd
import seaborn as sns
import mlflow
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from skops import io as skops_io
import joblib


# setup mlflow
mlflow.sklearn.autolog()
mlflow.set_tracking_uri("http://localhost:5000")


try:
    df = pd.read_csv('../data/gender.csv')
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
    "Logistic Regression": LogisticRegression(), #LogisticRegression(max_iter=200)
    "K-Nearest Neighbors (KNN)": KNeighborsClassifier(), #KNeighborsClassifier(n_neighbors=5)
    "Gaussian Naive Bayes": GaussianNB(),
    "Bernoulli Naive Bayes": BernoulliNB(),
    "Multinomial Naive Bayes": MultinomialNB(),
    "Decision Tree": DecisionTreeClassifier(),
}

results = []
with mlflow.start_run():
    for name, model in models.items():
        print(f"Melatih model {name}...")
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average="weighted")
        rec = recall_score(y_test, y_pred, average="weighted")
        f1 = f1_score(y_test, y_pred, average="weighted")

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

results_df = pd.DataFrame(results, columns=["Model", "Accuracy", "Precision", "Recall", "F1-Score"])
results_df.to_csv("../results/csv/evaluation_metrics.csv", index=False)
print("Evaluasi disimpan di results/csv/evaluation_metrics.csv")

# plt.tight_layout(rect=[0, 0, 1, 0.95])
# plt.show()