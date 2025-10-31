
# Step 1: Import Required Libraries ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from datetime import datetime

# === Step 2: Load Dataset ===
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

print("=== AI in Software Engineering - Task 3: Predictive Analytics ===")
print("Dataset loaded successfully.")
print(f"Shape: {df.shape}")
print(df.head())

# === Step 3: Split Dataset ===
X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === Step 4: Data Normalization ===
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# === Step 5: Train Model ===
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# === Step 6: Evaluate Model ===
y_pred = model.predict(X_test_scaled)

acc = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)

print("\nModel Accuracy: {:.2f}%".format(acc * 100))
print("\nClassification Report:\n", report)
print("\nConfusion Matrix:\n", matrix)

# === Step 7: Visualization ===
plt.figure(figsize=(6, 4))
sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["Benign", "Malignant"], yticklabels=["Benign", "Malignant"])
plt.title("Confusion Matrix Heatmap")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("task3_confusion_matrix.png")
plt.close()

# === Step 8: Save results to text file ===
results_file = "task3_results.txt"
with open(results_file, "w", encoding="utf-8") as f:
    f.write("=== Task 3: Predictive Analytics Results ===\n")
    f.write(f"Run timestamp: {datetime.now()}\n")
    f.write(f"Model Used: RandomForestClassifier\n")
    f.write(f"Accuracy: {acc*100:.2f}%\n\n")
    f.write("Classification Report:\n")
    f.write(report)
    f.write("\nConfusion Matrix:\n")
    f.write(np.array2string(matrix))

print(f"\n✅ Results saved to {results_file}")
print("✅ Confusion matrix saved as task3_confusion_matrix.png")
