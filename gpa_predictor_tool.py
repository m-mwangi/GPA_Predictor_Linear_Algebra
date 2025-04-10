import streamlit as st
import numpy as np

# Define the beta coefficients (from the model you trained)
beta = np.array([0.3690129, 0.01926417, 0.01280503, 0.09759901, 0.05214934, 
                 -0.08422138, 0.46388344, -0.03180732, 0.08167594])

# Function to predict GPA
def predict_gpa(study_hours_per_week, attendance, tutoring_sessions, sleep_hours,
                number_of_courses, past_gpa, relationship_status, extracurricular):
    input_features = np.array([
        1,  # Bias term
        study_hours_per_week,
        attendance,
        tutoring_sessions,
        sleep_hours,
        number_of_courses,
        past_gpa,
        relationship_status,
        extracurricular
    ])
    
    predicted_gpa = np.dot(input_features, beta)
    predicted_gpa = np.clip(predicted_gpa, 0.0, 4.0)  # Ensure GPA is between 0 and 4
    return predicted_gpa

# Streamlit app layout
st.set_page_config(page_title="GPA Predictor", page_icon="📚", layout="wide")

# Title and Description with Enhanced Colors and Background
st.markdown("""
    <style>
        .title {
            background-color: #4A90E2;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-size: 2.5em;
        }
        .subtitle {
            background-color: #F5A623;
            padding: 10px;
            border-radius: 10px;
            color: white;
            font-size: 1.5em;
        }
        .section-header {
            color: #4A90E2;
            font-size: 1.8em;
        }
        .section-content {
            font-size: 1.1em;
            line-height: 1.6;
        }
        .predict-button {
            background-color: #4A90E2;
            color: white;
            padding: 10px 20px;
            font-size: 1.1em;
            border-radius: 5px;
        }
        .info-box {
            border-radius: 10px;
            padding: 15px;
            background-color: #F1F8FF;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .footer {
            background-color: #4A90E2;
            padding: 10px;
            text-align: center;
            color: white;
            font-size: 1.2em;
        }
    </style>
    <div class="title">📚 **GPA Predictor Tool**</div>
""", unsafe_allow_html=True)

# Section: About the Tool
st.markdown("<h3 class='section-header'>🌟 About the Tool</h3>", unsafe_allow_html=True)
st.markdown("""
    <div class="section-content">
    This **GPA Predictor Tool** helps you estimate your **Final GPA** based on several factors, including:
    - **Study Hours per Week**
    - **Class Attendance**
    - **Tutoring Sessions**
    - **Sleep Hours**
    - **Number of Courses**
    - **Past GPA**
    - **Relationship Status**
    - **Extracurricular Activities**
    
    By inputting these details, you can get a prediction of your GPA on a scale of **0.0 to 4.0**.  
    **Note:** While it's a good estimate, remember that other factors (e.g., personal health, etc.) could affect your GPA!
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Section: About the Model
st.markdown("<h3 class='section-header'>🔎 About the Model</h3>", unsafe_allow_html=True)
st.markdown("""
    <div class="section-content">
    This tool applies **linear algebra** concepts to predict a student's GPA using a **linear regression** model. The process involved:
    1. **Data Collection**
    2. **Model Training**
    3. **Prediction**
    
    The prediction formula is:
    ```GPA = β0 + β1 * Study Hours + β2 * Attendance + ...```
    **Note:** This tool provides an estimate and should not be considered 100% accurate.
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Section: GPA Prediction
st.markdown("<h3 class='section-header'>🔮 GPA Prediction</h3>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Enter Your Information:")
    
    # User Input Fields
    study_hours_per_week = st.slider("📚 Study Hours per Week", min_value=0, max_value=168, value=20)
    attendance = st.slider("📊 Class Attendance (%)", min_value=0.0, max_value=100.0, value=75.0)
    tutoring_sessions = st.slider("🧑‍🏫 Tutoring Sessions", min_value=0, max_value=10, value=2)
    sleep_hours = st.slider("💤 Sleep Hours per Night", min_value=0, max_value=24, value=7)
    number_of_courses = st.slider("📘 Number of Courses", min_value=1, max_value=10, value=5)
    past_gpa = st.slider("🎓 Past GPA", min_value=0.0, max_value=4.0, value=2.5)
    relationship_status = st.selectbox("❤️ Relationship Status", ["Single", "In a relationship"])
    extracurricular = st.selectbox("🏅 Extracurricular Activities", ["No", "Yes"])

    # Convert categorical variables to numerical values
    relationship_status = 1 if relationship_status == "In a relationship" else 0
    extracurricular = 1 if extracurricular == "Yes" else 0

    # Button to trigger the prediction
    if st.button("🔮 **Predict GPA**", key="predict-btn"):
        predicted_gpa = predict_gpa(
            study_hours_per_week, 
            attendance, 
            tutoring_sessions, 
            sleep_hours, 
            number_of_courses, 
            past_gpa, 
            relationship_status, 
            extracurricular
        )
        
        # Display the result
        st.subheader("🔮 **Predicted GPA:**")
        st.write(f"Your predicted GPA is: **{predicted_gpa:.2f}**", unsafe_allow_html=True)
        st.success("Prediction successful! 🎉")

st.markdown("---")

# Contact Section
st.markdown("<div class='footer'>📬 **Contact:** gpa.predictor@edu.com</div>", unsafe_allow_html=True)
