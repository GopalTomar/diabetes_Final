import streamlit as st
from Govind_Notes_Diabetes import show_precautions_for_diabetic, show_precautions_for_non_diabetic

def predict_diabetes(diabetes_model):
    st.header('', divider='rainbow')
    st.title('Diabetes Prediction')
    st.markdown("<a href='https://www.who.int/health-topics/diabetes?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFo7LrTeJB-YF0RNzx4PNSP8kQ4Su3WoI3-ebQly1gtgOlsYfhejmmuhoCx6UQAvD_BwE#tab=tab_1'>To know More about Diabetes</a>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    placeholder_values = {
        'Pregnancies': 'Enter number of pregnancies (0-17)',
        'Glucose': 'Enter glucose level (0-200)',
        'Blood Pressure': 'Enter blood pressure (0-122)',
        'Skin Thickness': 'Enter skin thickness (0-99)',
        'Insulin': 'Enter insulin level (0-846)',
        'BMI': 'Enter BMI (0.0-60.0)',
        'Diabetes Pedigree Function': 'Enter diabetes pedigree function (0.0-2.5)',
        'Age': 'Enter age (0-122)'
    }

    diab_prediction = None  # Initialize diab_prediction variable

    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=17, format="%d",
                                  help=placeholder_values['Pregnancies'])
    col1, col2, col3 = st.columns(3)

    # Getting the input data from the user arranged in three columns
    with col1:
        glucose = st.number_input('Glucose', min_value=0, max_value=200, format="%d",
                                  help=placeholder_values['Glucose'])
        if glucose < 0 or glucose > 200:
            st.warning("Please enter glucose level within the range of 0 to 200.")
        
        blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=122,
                                         format="%d", help=placeholder_values['Blood Pressure'])
        if blood_pressure < 0 or blood_pressure > 122:
            st.warning("Please enter blood pressure within the range of 0 to 122.")
        
        skin_thickness = st.number_input('Skin Thickness', min_value=0, max_value=99,
                                         format="%d", help=placeholder_values['Skin Thickness'])
        if skin_thickness < 0 or skin_thickness > 99:
            st.warning("Please enter skin thickness within the range of 0 to 99.")

    with col2:
        insulin = st.number_input('Insulin', min_value=0, max_value=846, format="%d",
                                  help=placeholder_values['Insulin'])
        if insulin < 0 or insulin > 846:
            st.warning("Please enter insulin level within the range of 0 to 846.")
        
        bmi = st.number_input('BMI', min_value=0.0, max_value=60.0, format="%f",
                              help=placeholder_values['BMI'])
        if bmi < 0.0 or bmi > 60.0:
            st.warning("Please enter BMI within the range of 0.0 to 60.0.")

    with col3:
        diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5,
                                                     format="%f", help=placeholder_values['Diabetes Pedigree Function'])
        if diabetes_pedigree_function < 0.0 or diabetes_pedigree_function > 2.5:
            st.warning("Please enter diabetes pedigree function within the range of 0.0 to 2.5.")
        
        age = st.number_input('Age', min_value=0, max_value=122, format="%d",
                              help=placeholder_values['Age'])
        if age < 0 or age > 122:
            st.warning("Please enter age within the range of 0 to 122.")

    # Code for Prediction
    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin,
                      bmi, diabetes_pedigree_function, age]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'You are Diabetic'
        else:
            diab_diagnosis = 'You are NOT Diabetic'
        st.markdown("<a href='https://www.who.int/health-topics/diabetes?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFo7LrTeJB-YF0RNzx4PNSP8kQ4Su3WoI3-ebQly1gtgOlsYfhejmmuhoCx6UQAvD_BwE#tab=tab_1'>To know More</a>", unsafe_allow_html=True)
    st.success(diab_diagnosis)

    if diab_prediction is not None:
        if diab_prediction[0] == 1:
            show_precautions_for_diabetic()
            st.markdown("<a href='https://www.who.int/health-topics/diabetes?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFo7LrTeJB-YF0RNzx4PNSP8kQ4Su3WoI3-ebQly1gtgOlsYfhejmmuhoCx6UQAvD_BwE#tab=tab_1'>To know More</a>", unsafe_allow_html=True)
        else:
            show_precautions_for_non_diabetic()
            st.markdown("<a href='https://www.who.int/health-topics/diabetes?gad_source=1&gclid=CjwKCAjw_e2wBhAEEiwAyFFFo7LrTeJB-YF0RNzx4PNSP8kQ4Su3WoI3-ebQly1gtgOlsYfhejmmuhoCx6UQAvD_BwE#tab=tab_1'>To know More about Diabetes</a>", unsafe_allow_html=True)


def main():
    # Add your main function code here

    if __name__ == "__main__":
        main()
