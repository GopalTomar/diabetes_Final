import streamlit as st

def predict_kidney_disease(kidney_model):
    # Page title
    st.header('', divider='rainbow')
    st.title('Kidney Disease Prediction')
    st.markdown("<a href='https://www.cdc.gov/kidneydisease/basics.html#:~:text=CKD%20is%20a%20condition%20in,as%20heart%20disease%20and%20stroke./'>To know More about Kidney Disease</a>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    # Placeholder values for each input field
    placeholder_values = {
        'age': 'Enter age (0-122)',
        'bp': 'Enter blood pressure (0-122)',
        'sg': 'Enter specific gravity (0.0-2.0)',
        'al': 'Enter albumin (0-5)',
        'su': 'Enter sugar (0-5)',
        'rbc': 'Enter red blood cells (e.g., normal, abnormal)',
        'pc': 'Enter pus cell (e.g., normal, abnormal)',
        'pcc': 'Enter pus cell clumps (e.g., present, not present)',
        'ba': 'Enter bacteria (e.g., present, not present)',
        'bgr': 'Enter blood glucose random',
        'bu': 'Enter blood urea',
        'sc': 'Enter serum creatinine',
        'sod': 'Enter sodium',
        'pot': 'Enter potassium',
        'hemo': 'Enter hemoglobin',
        'pcv': 'Enter packed cell volume',
        'wc': 'Enter white blood cell count',
        'rc': 'Enter red blood cell count',
        'htn': 'Enter hypertension (e.g., yes, no)',
        'dm': 'Enter diabetes mellitus (e.g., yes, no)',
        'cad': 'Enter coronary artery disease (e.g., yes, no)',
        'appet': 'Enter appetite (e.g., good, poor)',
        'pe': 'Enter pedal edema (e.g., yes, no)',
        'ane': 'Enter anemia (e.g., yes, no)'
    }

    # Initialize kidney_prediction with a default value
    kidney_prediction = None

    # Getting the input data from the user arranged in three columns
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', min_value=0, max_value=122, format="%d",
                              help=placeholder_values['age'])
        if age < 0 or age > 122:
            st.warning("Please enter age within the range of 0 to 122.")

        bp = st.number_input('Blood Pressure', min_value=0, max_value=122,
                             format="%d", help=placeholder_values['bp'])
        if bp < 0 or bp > 122:
            st.warning("Please enter blood pressure within the range of 0 to 122.")

        sg = st.number_input('Specific Gravity', min_value=0.0, max_value=2.0,
                             format="%f", help=placeholder_values['sg'])
        if sg < 0.0 or sg > 2.0:
            st.warning("Please enter specific gravity within the range of 0.0 to 2.0.")

    with col2:
        al = st.number_input('Albumin', min_value=0, max_value=5,
                             format="%d", help=placeholder_values['al'])
        if al < 0 or al > 5:
            st.warning("Please enter albumin level within the range of 0 to 5.")

        su = st.number_input('Sugar', min_value=0, max_value=5,
                             format="%d", help=placeholder_values['su'])
        if su < 0 or su > 5:
            st.warning("Please enter sugar level within the range of 0 to 5.")

        rbc = st.text_input('Red Blood Cells', help=placeholder_values['rbc'])

    with col3:
        pc = st.text_input('Pus Cell', help=placeholder_values['pc'])
        pcc = st.text_input('Pus Cell Clumps', help=placeholder_values['pcc'])
        ba = st.text_input('Bacteria', help=placeholder_values['ba'])

    col4, col5, col6 = st.columns(3)

    with col4:
        bgr = st.number_input('Blood Glucose Random',
                              help=placeholder_values['bgr'])
        hemo = st.number_input('Hemoglobin', help=placeholder_values['hemo'])


    with col5:
        bu = st.number_input('Blood Urea', help=placeholder_values['bu'])
        sc = st.number_input('Serum Creatinine', help=placeholder_values['sc'])


    with col6:
        sod = st.number_input('Sodium', help=placeholder_values['sod'])
        pot = st.number_input('Potassium', help=placeholder_values['pot'])

    # Code for Prediction
    kidney_diagnosis = ''

    # Creating a button for Prediction
    if st.button("Predict Kidney Disease"):
        user_input = [age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo]

        kidney_prediction = kidney_model.predict([user_input])

        if kidney_prediction[0] == 1:
            kidney_diagnosis = 'Patient has Kidney Disease'
        else:
            kidney_diagnosis = 'Patient does not have Kidney Disease'
        st.markdown("<a href='https://www.cdc.gov/kidneydisease/basics.html#:~:text=CKD%20is%20a%20condition%20in,as%20heart%20disease%20and%20stroke./'>To know More</a>", unsafe_allow_html=True)


    # Display diagnosis
    st.success(kidney_diagnosis)

# if __name__ == "__main__":
#     # Sample model for demonstration
#     kidney_model = None
#     predict_kidney_disease(kidney_model)
