import streamlit as st
import numpy as np

# Define the beta coefficients (from the model you trained)
beta = np.array([ 0.02034646,  0.01510517,  0.09826161,  0.05763991, -0.07892038, 
                 0.49194746, -0.02928652,  0.08499642,  0.0145018 ])  # Update this with the correct values

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

# Title and Description
st.title("📚 GPA Predictor Tool")
st.markdown("""
This **GPA Predictor Tool** helps you estimate your **Final GPA** based on several factors, including:

- Study Hours per Week
- Attendance
- Tutoring Sessions
- Sleep Hours
- Number of Courses
- Past GPA
- Relationship Status
- Extracurricular Activities

By inputting these details, you can get a prediction of your GPA on a scale of 0 to 4.0.
""")
st.markdown("---")

# Create a two-column layout for input form and result
col1, col2 = st.columns([2, 1])

with col1:
    # Interactive Form to Get User Input
    st.subheader("Enter Your Information:")

    # User Input Fields
    study_hours_per_week = st.number_input("Study Hours per Week", min_value=0.0, max_value=168.0, value=20.0, step=0.5)
    attendance = st.number_input("Class Attendance (%)", min_value=0.0, max_value=100.0, value=75.0, step=0.1)
    tutoring_sessions = st.number_input("Tutoring Sessions", min_value=0, max_value=10, value=2)
    sleep_hours = st.number_input("Sleep Hours per Night", min_value=0.0, max_value=24.0, value=7.0, step=0.5)
    number_of_courses = st.number_input("Number of Courses", min_value=1, max_value=10, value=5)
    past_gpa = st.number_input("Past GPA", min_value=0.0, max_value=4.0, value=2.5, step=0.1)
    relationship_status = st.selectbox("Relationship Status", ["Single", "In a relationship"])
    extracurricular = st.selectbox("Extracurricular Activities", ["No", "Yes"])

    # Convert categorical variables to numerical values
    relationship_status = 1 if relationship_status == "In a relationship" else 0
    extracurricular = 1 if extracurricular == "Yes" else 0

    # Button to trigger the prediction
    if st.button("Predict GPA"):
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
        st.subheader("Predicted GPA:")
        st.write(f"Your predicted GPA is: **{predicted_gpa:.2f}**")
        st.success("Prediction successful!")

with col2:
    # Display some visuals (example: GPA prediction explanation)
    st.image("https://via.placeholder.com/200x200.png?text=GPA+Predictor", use_column_width=True)
    st.markdown("""
    ### About the GPA Predictor:
    - The GPA Predictor uses data such as study hours, class attendance, and past GPA to estimate your final GPA.
    - It is based on a **linear regression model** that factors in key academic and personal factors.
    - While it's a good estimate, remember that other factors could affect your GPA as well!
    """)
    
    st.markdown("---")
    st.markdown("### About the Model:")
    st.markdown("""
    This tool uses **Linear Regression** to predict GPA. The model was trained using historical student data. It calculates the GPA prediction using a set of features and returns a result within the range of 0.0 to 4.0.

    The prediction formula is:
    ```
    GPA = w0 + w1 * Study Hours + w2 * Attendance + w3 * Tutoring Sessions + ...
    ```
    Each weight (w) is determined during the model training process.

    **Important**: This tool serves as a prediction and should not be considered 100% accurate.
    """)

    st.markdown("---")
    st.markdown("### Contact:")
    st.markdown("For any questions or feedback, reach out at [gpa.predictor@edu.com](mailto:gpa.predictor@edu.com)")

# Footer (Optional)
st.markdown("---")
st.markdown("Made with ❤️ by [Your Name].")
