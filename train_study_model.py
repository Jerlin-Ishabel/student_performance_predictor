# train_model.py

import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("Student_Performance_Study.csv")

# Encode categorical columns
le = LabelEncoder()
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Split features and labels
X = df.drop("Performance", axis=1)
y = df["Performance"]
y = le.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Save model and scaler
os.makedirs("model9", exist_ok=True)
joblib.dump(model, "model9/trained_model9.pkl")
joblib.dump(scaler, "model9/scaler9.pkl")

print("✅ Model and scaler saved in 'model9/' folder.")
