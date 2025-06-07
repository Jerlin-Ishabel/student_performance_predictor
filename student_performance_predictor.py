import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from datetime import datetime

# 🎨 Blinking CSS style
st.markdown("""
<style>
@keyframes colorBlink {
  0% {color: red;}
  25% {color: green;}
  50% {color: blue;}
  75% {color: orange;}
}
.color-blink {
  animation: colorBlink 1s infinite;
  text-align: center;
  font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 🧠 Load model and scaler
model_path = os.path.join("model9", "trained_model9.pkl")
scaler_path = os.path.join("model9", "scaler9.pkl")

def load_model():
    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        st.error("🚫 Model or scaler file missing. Please check the 'model9/' directory.")
        st.stop()
    return joblib.load(model_path), joblib.load(scaler_path)

model, scaler = load_model()

# 🎓 Title Section
st.markdown("""
<div style="background-color:#f0f8ff; padding:10px; border-radius:10px;">
<h2 class="color-blink">🎓 Student Performance Predictor Based on Study Habits</h2>
</div>
""", unsafe_allow_html=True)

st.title("📋 Enter Your Study Habits")

# 📥 Input Section
age = st.number_input("Age", 10, 100, 20)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
study_hours = st.slider("Study Hours", 1, 16, 3)
sleep_quality = st.slider("Sleep Quality (1-10)", 1, 10, 5)
focus = st.slider("Focus Level (1-10)", 1, 10, 5)
mood = st.slider("Mood Level (1-10)", 1, 10, 5)
device_used = st.selectbox("Device Used", ["Mobile", "Laptop", "Tablet", "Desktop"])
study_goal = st.selectbox("Study Goal", ["Pass Exam", "Top Rank", "Clear Doubts", "Daily Study"])
lighting = st.selectbox("Lighting", ["Natural", "Artificial"])
noise = st.selectbox("Background Noise", ["Quiet", "Noise"])
note_method = st.selectbox("Note Taking Method", ["Digital", "Paper", "None"])
session_type = st.selectbox("Session Type", ["Group", "Solo"])
major = st.selectbox("Major", ["Science", "Commerce", "Arts"])
internet_use = st.selectbox("Internet Use", ["Online Class", "Social Media", "Both"])
retention_score = st.slider("Retention Score (%)", 0, 100, 60)

# 🔁 Encode input
gender_map = {"Male": 0, "Female": 1, "Other": 2}
device_map = {"Mobile": 0, "Laptop": 1, "Tablet": 2, "Desktop": 3}
study_goal_map = {"Pass Exam": 0, "Top Rank": 1, "Clear Doubts": 2, "Daily Study": 3}
lighting_map = {"Natural": 0, "Artificial": 1}
noise_map = {"Quiet": 0, "Noise": 1}
note_map = {"Digital": 0, "Paper": 1, "None": 2}
session_map = {"Group": 0, "Solo": 1}
major_map = {"Science": 0, "Commerce": 1, "Arts": 2}
internet_map = {"Online Class": 0, "Social Media": 1, "Both": 2}

input_data = np.array([[
    age,
    gender_map[gender],
    study_hours,
    sleep_quality,
    focus,
    mood,
    device_map[device_used],
    study_goal_map[study_goal],
    lighting_map[lighting],
    noise_map[noise],
    note_map[note_method],
    session_map[session_type],
    major_map[major],
    internet_map[internet_use],
    retention_score
]])

try:
    input_scaled = scaler.transform(input_data)
except Exception as e:
    st.error(f"❌ Error while scaling input: {e}")
    st.stop()

performance_labels = {0: "Low", 1: "Moderate", 2: "High"}

if st.button("📊 Predict Performance"):
    prediction = model.predict(input_scaled)[0]
    pred_label = performance_labels.get(int(prediction), "Unknown")
    st.success(f"🎯 Predicted Performance: **{pred_label}**")

    user_input = {
        "Age": age,
        "Gender": gender,
        "Study Hours": study_hours,
        "Sleep Quality": sleep_quality,
        "Focus Level": focus,
        "Mood": mood,
        "Device Used": device_used,
        "Study Goal": study_goal,
        "Lighting": lighting,
        "Background Noise": noise,
        "Note Taking Method": note_method,
        "Session Type": session_type,
        "Major": major,
        "Internet Use": internet_use,
        "Retention Score": retention_score
    }

    def generate_pdf(pred_label, inputs):
        filename = "Student_Performance_Report.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(colors.darkblue)
        c.drawString(150, height - 50, "📘 Student Performance Report")

        c.setFont("Helvetica", 10)
        c.setFillColor(colors.black)
        c.drawString(400, height - 20, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

        y = height - 90
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(colors.green)
        c.drawString(50, y, "📝 Input Summary:")
        y -= 20

        c.setFont("Helvetica", 11)
        for key, val in inputs.items():
            c.drawString(60, y, f"{key}: {val}")
            y -= 15

        y -= 20
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(colors.darkred)
        c.drawString(50, y, "🎯 Predicted Performance:")
        y -= 20
        c.setFont("Helvetica", 12)
        c.drawString(60, y, f"Level: {pred_label}")

        # Study Tips based on prediction
        y -= 30
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(colors.navy)
        c.drawString(50, y, "✅ Study Tips:")
        y -= 20
        c.setFont("Helvetica", 11)

        if pred_label == "Low":
            tips = [
                "📌 Maintain a consistent study routine",
                "📌 Reduce distractions like social media",
                "📌 Improve sleep and physical activity",
                "📌 Set small achievable study goals",
                "📌 Practice mindfulness to boost focus"
            ]
        elif pred_label == "Moderate":
            tips = [
                "✅ Stick to your study plan and improve gradually",
                "✅ Use effective note-taking techniques",
                "✅ Prioritize understanding over memorization",
                "✅ Create a calm and well-lit study space",
                "✅ Take breaks to avoid burnout"
            ]
        else:
            tips = [
                "🌟 Keep up your effective study habits!",
                "🌟 Help peers and revise regularly",
                "🌟 Try peer teaching to reinforce knowledge",
                "🌟 Focus on advanced practice problems",
                "🌟 Maintain balance with sleep and breaks"
            ]

        for tip in tips:
            c.drawString(60, y, tip)
            y -= 15

        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(colors.darkgreen)
        y -= 30
        c.drawString(100, y, "🙏 Thank you for using the Predictor!")

        c.save()
        return filename

    pdf_file = generate_pdf(pred_label, user_input)
    with open(pdf_file, "rb") as file:
        st.download_button("📄 Download Report as PDF", file, file_name=pdf_file, mime="application/pdf")

# 📊 Visualization Section
st.title("📈 Dataset Visualization")
df_path = "Student_Performance_Study.csv"
if os.path.exists(df_path):
    df = pd.read_csv(df_path)
    with st.expander("🔍 View Dataset Summary"):
        st.dataframe(df.head(10))
        st.write(df.describe())

    st.subheader("📊 Key Visual Insights")

    # Performance Distribution
    fig1, ax1 = plt.subplots()
    sns.countplot(data=df, x="Performance", palette="Set2", ax=ax1)
    ax1.set_title("Performance Distribution")
    st.pyplot(fig1)

    # Study Hours vs Retention Score
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x="Study_Hours", y="Retention_Score", hue="Performance", palette="coolwarm", ax=ax2)
    ax2.set_title("Study Hours vs Retention Score")
    st.pyplot(fig2)

    # Correlation Heatmap
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="YlGnBu", ax=ax3)
    ax3.set_title("Feature Correlation Heatmap")
    st.pyplot(fig3)
else:
    st.warning("⚠️ Dataset not found! Please ensure 'Student_Performance_Study.csv' is in the app folder.")
