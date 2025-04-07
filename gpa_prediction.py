import streamlit as st
import numpy as np

# Define beta coefficients from your model
beta = [
    0.60486867,  # Intercept
    0.04368508,  # Study Hours
    0.02033073,  # Attendance Rate
    0.30040298,  # Past GPA
    -0.04936169, # Number of Courses
    0.05093152,  # Extracurricular Activities
    -0.08173411  # Dating Status
]

# Function to predict GPA
def predict_gpa(study_hours, attendance_rate, past_gpa, num_courses, extracurricular, dating):
    features = np.array([1, study_hours, attendance_rate, past_gpa, num_courses, extracurricular, dating])
    predicted_gpa = np.dot(features, beta)
    return predicted_gpa

# Title and Layout with Enhanced Color and Fun Instructions
st.markdown("""
    <style>
        .title {
            font-size: 50px;
            color: #1abc9c;
            font-weight: bold;
            text-align: center;
            font-family: 'Arial', sans-serif;
        }
        .instructions {
            font-size: 22px;
            color: #3498db;
            font-style: italic;
            text-align: center;
        }
        .warning {
            font-size: 18px;
            color: #e74c3c;
            text-align: center;
        }
        .section {
            background-color: #ecf0f1;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎓 Welcome to the GPA Predictor Tool!</div>', unsafe_allow_html=True)

st.markdown('<div class="instructions">Fill in the details displayed and let us predict your GPA! </div>', unsafe_allow_html=True)

st.markdown('<div class="warning">⚠️ Be honest, the numbers you input will directly affect your prediction!</div>', unsafe_allow_html=True)

# Inputs in a sidebar with enhanced color
st.sidebar.markdown("<h3 style='color:#16a085;'>📊 Please Enter Your Information:</h3>", unsafe_allow_html=True)
study_hours = st.sidebar.number_input("Study Hours 🕒", min_value=0, max_value=24, value=8, step=1)
attendance_rate = st.sidebar.number_input("Attendance Rate (%) 📅", min_value=0, max_value=100, value=85, step=1)
past_gpa = st.sidebar.number_input("Past GPA 📚", min_value=0.0, max_value=4.0, value=3.0, step=0.1)
num_courses = st.sidebar.number_input("Number of Courses 🏫", min_value=1, max_value=10, value=5)
extracurricular = st.sidebar.selectbox("Extracurricular Activities 🎭", ["Yes", "No"])
dating = st.sidebar.selectbox("Dating Status 💖", ["Yes", "No"])

# Convert "Yes" to 1 and "No" to 0
extracurricular = 1 if extracurricular == "Yes" else 0
dating = 1 if dating == "Yes" else 0

# Button to trigger prediction
if st.sidebar.button("Predict My GPA! 🎯"):
    with st.spinner('Calculating your GPA...'):
        predicted_gpa = predict_gpa(study_hours, attendance_rate, past_gpa, num_courses, extracurricular, dating)
    st.success(f"🎉 Your Predicted GPA is: {predicted_gpa:.2f}")
