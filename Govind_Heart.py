import streamlit as st

def predict_heart(heart_disease_model):

    st.header('', divider='rainbow')
    st.title('Heart Disease Prediction')
    st.markdown("<a href='https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFoyHzJIf4JMBxGL3OJRkzF9Zxc3nb9v1RtM_-m7M3OuaYtrwWnbSVMBoCTNQQAvD_BwE/'>To know More about Heart Disease</a>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    # Input fields
    row1, row2, row3 = st.columns(3)
    
    with row1:
        age = st.text_input('Age', placeholder='Enter age (e.g., 30)', help='Please enter the age of the patient.')
        cp = st.selectbox('Chest Pain Types', [0, 1, 2, 3], format_func=lambda x: f'CP {x}', help='Please select the type of chest pain.')
        trestbps = st.text_input('Resting Blood Pressure', placeholder='Enter blood pressure (e.g., 120)', help='Please enter the resting blood pressure.')
        chol = st.text_input('Serum Cholesterol (mg/dl)', placeholder='Enter cholesterol level (e.g., 200)', help='Please enter the serum cholesterol level.')
        sex = st.radio('Sex', ['Female', 'Male'], help='Please select the gender of the patient.')
    
    with row2:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['No', 'Yes'], index=0, help='Please select if the fasting blood sugar is greater than 120 mg/dl.')
        restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2], format_func=lambda x: f'Result {x}', help='Please select the resting electrocardiographic result.')
        thalach = st.text_input('Maximum Heart Rate Achieved', placeholder='Enter heart rate (e.g., 150)', help='Please enter the maximum heart rate achieved.')
        exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'], index=0, help='Please select if the patient has exercise induced angina.')
    
    with row3:
        oldpeak = st.text_input('ST Depression Induced by Exercise', placeholder='Enter ST depression value (e.g., 1.0)', help='Please enter the ST depression induced by exercise relative to rest.')
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2], format_func=lambda x: f'Slope {x}', help='Please select the slope of the peak exercise ST segment.')
        ca = st.selectbox('Major Vessels Colored by Fluoroscopy', [0, 1, 2, 3], format_func=lambda x: f'Vessels {x}', help='Please select the number of major vessels colored by fluoroscopy.')
        thal = st.selectbox('Thal', [0, 1, 2, 3], format_func=lambda x: f'Thal {x}', help='Please select the Thal value.')
    

    if st.button('Predict Heart Disease'):
  
        if '' in [age, trestbps, chol, thalach, oldpeak]:
            st.warning('Please fill in all the fields.')
            return
        
        # Convert inputs to numeric values
        age = float(age)
        sex = 1 if sex == 'Male' else 0
        trestbps = float(trestbps)
        chol = float(chol)
        restecg = int(restecg)
        thalach = float(thalach)
        exang = 1 if exang == 'Yes' else 0
        oldpeak = float(oldpeak)
        

        fbs = 1 if fbs == 'Yes' else 0
        
   
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        
        # Perform prediction
        heart_prediction = heart_disease_model.predict([user_input])

        # Display result
        if heart_prediction[0] == 1:
            st.success('The person is predicted to have heart disease.')
            st.markdown("<a href='https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFoyHzJIf4JMBxGL3OJRkzF9Zxc3nb9v1RtM_-m7M3OuaYtrwWnbSVMBoCTNQQAvD_BwE'>To know More about Heart Disease</a>", unsafe_allow_html=True)
        else:
            st.success('The person is predicted to not have heart disease.')
            st.markdown("<a href='https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFoyHzJIf4JMBxGL3OJRkzF9Zxc3nb9v1RtM_-m7M3OuaYtrwWnbSVMBoCTNQQAvD_BwE'>To know More about Heart Disease</a>", unsafe_allow_html=True)


if __name__ == "__main__":
    heart_disease_model = None
    predict_heart(heart_disease_model)
