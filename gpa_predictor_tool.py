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
st.title("📚 **GPA Predictor Tool**")
st.markdown("""
    <style>
        .header-background {
            background-color: #4A90E2;
            padding: 25px;
            border-radius: 12px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        .subheader {
            color: #4A90E2;
        }
        .section-background {
            background-color: #f7f7f7;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #4A90E2;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #357ABD;
        }
    </style>
    <div class="header-background">
        <h2>Estimate Your Final GPA Based on Key Factors</h2>
        <h4>"Math meets life. Predict your GPA, shape your strategy."</h4>
    </div>
""", unsafe_allow_html=True)

# Section: About the Tool
st.markdown("<h3 class='subheader'>🌟 About the Tool</h3>", unsafe_allow_html=True)
st.markdown("""
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
""")
st.markdown("---")

# Section: About the Model
st.markdown("<h3 class='subheader'>🔎 About the Model</h3>", unsafe_allow_html=True)
st.markdown("""
    This tool applies **linear regression** to predict a student's GPA. The model uses a statistical method that models the relationship between a dependent variable (GPA) and several independent variables (such as study hours, attendance, etc.).

    The process involved:
    1. **Data Collection**: Historical data from students, covering their study habits, attendance, and past GPA.
    2. **Model Training**: The coefficients (weights) are learned by minimizing the prediction error.
    3. **Prediction**: The model predicts your GPA based on the formula:
    ``` 
    GPA = β0 + β1 * Study Hours + β2 * Attendance + β3 * Tutoring Sessions + ... 
    ```

    **Important:** This is a predictive tool, and the results should be treated as an estimate.
""")
st.markdown("---")

# Section: GPA Prediction
st.markdown("<h3 class='subheader'>🔮 GPA Prediction</h3>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Enter Your Information:")
    
    # User Input Fields in a more modern layout
    study_hours_per_week = st.number_input("📚 Study Hours per Week", min_value=0.0, max_value=168.0, value=20.0, step=0.5)
    attendance = st.number_input("📊 Class Attendance (%)", min_value=0.0, max_value=100.0, value=75.0, step=0.1)
    tutoring_sessions = st.number_input("🧑‍🏫 Tutoring Sessions", min_value=0, max_value=10, value=2)
    sleep_hours = st.number_input("💤 Sleep Hours per Night", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
    number_of_courses = st.number_input("📘 Number of Courses", min_value=1, max_value=10, value=5)
    past_gpa = st.number_input("🎓 Past GPA", min_value=0.0, max_value=4.0 , value=2.5, step=0.1)
    relationship_status = st.selectbox("❤️ Relationship Status", ["Single", "In a relationship"])
    extracurricular = st.selectbox("🏅 Extracurricular Activities", ["No", "Yes"])

    # Convert categorical variables to numerical values
    relationship_status = 1 if relationship_status == "In a relationship" else 0
    extracurricular = 1 if extracurricular == "Yes" else 0

    # Button to trigger the prediction
    if st.button("🔮 **Predict GPA**"):
        # Call the prediction function
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
st.markdown("### 📬 **Contact:**")
st.markdown("For any questions or feedback, reach out at [gpa.predictor@edu.com](mailto:gpa.predictor@edu.com)")

