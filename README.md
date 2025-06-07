

## 🎓 Project Overview

**Student Performance Predictor Based on Study Habits** is a Streamlit-based web application designed to predict a student's academic performance—categorized as **Low**, **Moderate**, or **High**—based on their study habits, lifestyle, and personal attributes.

This application leverages a **Logistic Regression** model trained on realistic academic behavior data. The system applies preprocessing techniques including label encoding and scaling, ensuring reliable predictions. A smooth and engaging user experience is enabled through an interactive web interface.

**Users can:**

* Enter personal, academic, and lifestyle data
* Instantly view predicted performance category
* Receive customized study tips
* Download a personalized report in PDF format

This project helps students understand how their daily habits influence academic outcomes, promoting self-awareness and data-driven academic planning.

---

## 🎯 Project Objectives

✅ **Academic Insight:** Predict performance categories using input features like study hours, mood, focus, sleep, and more.

✅ **User-Friendly Interface:** Provide a clean and intuitive UI using Streamlit for easy access on web.

✅ **Customized Tips:** Deliver actionable study tips based on prediction results.

✅ **PDF Report Generation:** Allow users to download a summary report of inputs, predictions, and tips.

✅ **Data Visualization:** Visualize study behaviors, performance patterns, and correlation between variables.

✅ **Machine Learning Integration:** Use a trained Logistic Regression model with proper scaling for accurate classification.

---

## ❗ Problem Statement

Many students struggle with academic performance due to inconsistent habits, poor focus, or lack of awareness about effective study methods. There is no simple, accessible tool to reflect how personal habits influence academic success.

---

## 💡 Proposed Solution

This web-based tool aims to provide personalized academic insight using machine learning:

* Predict performance level: **Low**, **Moderate**, or **High**
* Analyze features like study hours, sleep, mood, and focus
* Deliver personalized tips for academic improvement
* Enable report generation for tracking and sharing

This model empowers students to take control of their performance by understanding what really matters in their daily study routines.

---

## 🔄 Workflow of the Project

### 1. 📥 Data Collection

Collected data from students on study habits, mental focus, device use, sleep, and retention score.

### 2. 🧹 Data Preprocessing

* Removed duplicates and handled missing data
* Encoded categorical variables like gender and device
* Scaled data using StandardScaler

### 3. 🧠 Model Training

* Trained a Logistic Regression classifier
* Applied proper train-test split for validation

### 4. 📊 Data Visualization

* Generated visualizations (countplots, scatter plots, heatmaps) to explore insights

### 5. 🌐 Streamlit Web App

* Built an interactive form for inputs
* Displayed real-time prediction and study tips

### 6. 📄 PDF Report Generation

* Used ReportLab to generate downloadable performance reports

---

🔗 **Live Demo:** *https://studentperformancepredictor-ckrsydszmapaxqfimccrvm.streamlit.app/*

📁 **Dataset:** Student\_Performance\_Study.csv

📌 **Performance Levels:**

* `0 → Low`
* `1 → Moderate`
* `2 → High`

 | Tool / Library          | Purpose                             |
| ----------------------- | ----------------------------------- |
| **Python**              | Main programming language           |
| **Pandas, NumPy**       | Data manipulation                   |
| **scikit-learn**        | Machine learning model              |
| **Matplotlib, Seaborn** | Data visualization                  |
| **Streamlit**           | Web app frontend                    |
| **ReportLab**           | PDF report generation               |
| **Joblib**              | Saving and loading model and scaler |


📌 Conclusion
This project successfully demonstrates the power of machine learning in predicting real-life outcomes and promoting behavioral improvement. By creating a student-focused application, it not only empowers users to reflect on their habits but also encourages them to make data-backed changes to enhance their academic journey.

https://github.com/user-attachments/assets/7ea1130a-8018-43b2-8e27-de0cf4456dd9




