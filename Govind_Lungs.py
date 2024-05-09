import streamlit as st

def predict_lung_cancer(lung_cancer_model):

    st.header('', divider='rainbow')
    st.title('Lungs Cancer Prediction')
    st.markdown("<a href='https://www.niehs.nih.gov/health/topics/conditions/lung-disease'>To know More about Lungs Cancer</a>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # Input fields based on column names
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.text_input('Age', placeholder='Enter age')
        gender = st.radio('Gender', ['Female', 'Male'], index=1)  # Assuming index 1 corresponds to Male
        gender = 1 if gender == 'Male' else 0
        

    with col2:
        smoking = st.radio('Smoking', ['No', 'Yes'], index=0)  # Assuming index 0 corresponds to No
        smoking = 2 if smoking == 'Yes' else 1
        yellow_fingers = st.radio('Yellow Fingers', ['No', 'Yes'], index=0)
        yellow_fingers = 2 if yellow_fingers == 'Yes' else 1

    with col3:
        anxiety = st.radio('Anxiety', ['No', 'Yes'], index=0)
        anxiety = 2 if anxiety == 'Yes' else 1
        peer_pressure = st.radio('Peer Pressure', ['No', 'Yes'], index=0)
        peer_pressure = 2 if peer_pressure == 'Yes' else 1

    with col4:
        chronic_disease = st.radio('Chronic Disease', ['No', 'Yes'], index=0)
        chronic_disease = 2 if chronic_disease == 'Yes' else 1
        fatigue = st.radio('Fatigue', ['No', 'Yes'], index=0)
        fatigue = 2 if fatigue == 'Yes' else 1

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        allergy = st.radio('Allergy', ['No', 'Yes'], index=0)
        allergy = 2 if allergy == 'Yes' else 1
        wheezing = st.radio('Wheezing', ['No', 'Yes'], index=0)
        wheezing = 2 if wheezing == 'Yes' else 1

    with col6:
        alcohol = st.radio('Alcohol', ['No', 'Yes'], index=0)
        alcohol = 2 if alcohol == 'Yes' else 1
        coughing = st.radio('Coughing', ['No', 'Yes'], index=0)
        coughing = 2 if coughing == 'Yes' else 1

    with col7:
        shortness_of_breath = st.radio('Shortness of Breath', ['No', 'Yes'], index=0)
        shortness_of_breath = 2 if shortness_of_breath == 'Yes' else 1
        swallowing_difficulty = st.radio('Swallowing Difficulty', ['No', 'Yes'], index=0)
        swallowing_difficulty = 2 if swallowing_difficulty == 'Yes' else 1

    with col8:
        chest_pain = st.radio('Chest Pain', ['No', 'Yes'], index=0)
        chest_pain = 2 if chest_pain == 'Yes' else 1


    if st.button('Predict Lung Cancer'):

        if not age:
            st.warning("Please enter the age.")
            return


        age = float(age)

        user_input = [gender, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue,
                      allergy, wheezing, alcohol, coughing, shortness_of_breath, swallowing_difficulty, chest_pain]

        lung_cancer_prediction = lung_cancer_model.predict([user_input])

        if lung_cancer_prediction[0] == 1:
            st.success('The person is predicted to have lung cancer.')
            st.markdown("<a href='https://www.niehs.nih.gov/health/topics/conditions/lung-disease'>To know More about Lungs Cancer</a>", unsafe_allow_html=True)

        else:
            st.success('The person is predicted to not have lung cancer.')
            st.markdown("<a href='https://www.niehs.nih.gov/health/topics/conditions/lung-disease'>To know More about Lungs Cancer</a>", unsafe_allow_html=True)


if __name__ == "__main__":
    lung_cancer_model = None
    predict_lung_cancer(lung_cancer_model)
