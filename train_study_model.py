# train_study_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Step 1: Load Dataset
df = pd.read_csv("Student_Performance_Study.csv")

# Step 2: Drop missing values
df.dropna(inplace=True)

# Step 3: Encode categorical columns
label_encoders = {}
categorical_cols = df.select_dtypes(include='object').columns.drop("Performance")  # Exclude target

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Step 4: Encode target column
target_encoder = LabelEncoder()
df["Performance"] = target_encoder.fit_transform(df["Performance"])

# Step 5: Feature and Target split
X = df.drop("Performance", axis=1)
y = df["Performance"]

# Step 6: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 8: Model training
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Step 9: Evaluation
y_pred = model.predict(X_test_scaled)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Step 10: Save model and encoders
joblib.dump(model, "student_performance_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(label_encoders, "label_encoders.pkl")
joblib.dump(target_encoder, "target_encoder.pkl")

print("✅ Model and preprocessing files saved successfully.")
