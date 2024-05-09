import streamlit as st

def predict_parkinsons(parkinsons_model):
    st.header('', divider='rainbow')
    st.title("Parkinson's Disease Prediction")
    st.markdown("<a href='https://www.who.int/news-room/fact-sheets/detail/parkinson-disease#:~:text=Parkinson%20disease%20(PD)%20is%20a,muscle%20contractions%20and%20difficulty%20speaking.'>To know More about Parkinson</a>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    placeholder_values = {
        'MDVP:Fo(Hz)': 'Enter average vocal fundamental frequency (e.g., 119.992)',
        'MDVP:Fhi(Hz)': 'Enter maximum vocal fundamental frequency',
        'MDVP:Flo(Hz)': 'Enter minimum vocal fundamental frequency',
        'MDVP:Jitter(%)': 'Enter jitter percentage',
        'MDVP:Jitter(Abs)': 'Enter absolute jitter',
        'MDVP:RAP': 'Enter relative average perturbation',
        'MDVP:PPQ': 'Enter PPQ (pitch period perturbation quotient)',
        'Jitter:DDP': 'Enter DDP (jitter DDP)',
        'MDVP:Shimmer': 'Enter shimmer',
        'MDVP:Shimmer(dB)': 'Enter shimmer in dB',
        'Shimmer:APQ3': 'Enter APQ3 (amplitude perturbation quotient)',
        'Shimmer:APQ5': 'Enter APQ5 (amplitude perturbation quotient)',
        'MDVP:APQ': 'Enter APQ (amplitude perturbation quotient)',
        'Shimmer:DDA': 'Enter DDA (amplitude perturbation quotient)',
        'NHR': 'Enter NHR (noise-to-harmonics ratio)',
        'HNR': 'Enter HNR (harmonics-to-noise ratio)',
        'RPDE': 'Enter RPDE (recurrence period density entropy)',
        'DFA': 'Enter DFA (signal fractal scaling exponent)',
        'spread1': 'Enter spread1',
        'spread2': 'Enter spread2',
        'D2': 'Enter D2',
        'PPE': 'Enter PPE'
    }

    col1, col2, col3 = st.columns(3)
    with col1:
        fo = st.text_input('MDVP Fo(Hz)', placeholder=placeholder_values['MDVP:Fo(Hz)'], help='Help text here')
        fhi = st.text_input('MDVP Fhi(Hz)', placeholder=placeholder_values['MDVP:Fhi(Hz)'], help='Help text here')
        flo = st.text_input('MDVP Flo(Hz)', placeholder=placeholder_values['MDVP:Flo(Hz)'], help='Help text here')
        Jitter_percent = st.text_input('MDVP Jitter(%)', placeholder=placeholder_values['MDVP:Jitter(%)'], help='Help text here')
        Jitter_Abs = st.text_input('MDVP Jitter(Abs)', placeholder=placeholder_values['MDVP:Jitter(Abs)'], help='Help text here')
        RAP = st.text_input('MDVP RAP', placeholder=placeholder_values['MDVP:RAP'], help='Help text here')
        PPQ = st.text_input('MDVP PPQ', placeholder=placeholder_values['MDVP:PPQ'], help='Help text here')
        DDP = st.text_input('Jitter DDP', placeholder=placeholder_values['Jitter:DDP'], help='Help text here')

    with col2:
        Shimmer = st.text_input('MDVP Shimmer', placeholder=placeholder_values['MDVP:Shimmer'], help='Help text here')
        Shimmer_dB = st.text_input('MDVP Shimmer(dB)', placeholder=placeholder_values['MDVP:Shimmer(dB)'], help='Help text here')
        APQ3 = st.text_input('Shimmer APQ3', placeholder=placeholder_values['Shimmer:APQ3'], help='Help text here')
        APQ5 = st.text_input('Shimmer APQ5', placeholder=placeholder_values['Shimmer:APQ5'], help='Help text here')
        APQ = st.text_input('MDVP APQ', placeholder=placeholder_values['MDVP:APQ'], help='Help text here')
        DDA = st.text_input('Shimmer DDA', placeholder=placeholder_values['Shimmer:DDA'], help='Help text here')
        NHR = st.text_input('NHR', placeholder=placeholder_values['NHR'], help='Help text here')
        HNR = st.text_input('HNR', placeholder=placeholder_values['HNR'], help='Help text here')
        
    with col3:
        RPDE = st.text_input('RPDE', placeholder=placeholder_values['RPDE'], help='Help text here')
        DFA = st.text_input('DFA', placeholder=placeholder_values['DFA'], help='Help text here')
        spread1 = st.text_input('spread1', placeholder=placeholder_values['spread1'], help='Help text here')
        spread2 = st.text_input('spread2', placeholder=placeholder_values['spread2'], help='Help text here')
        D2 = st.text_input('D2', placeholder=placeholder_values['D2'], help='Help text here')
        PPE = st.text_input('PPE', placeholder=placeholder_values['PPE'], help='Help text here')
        status = st.radio('Status', ['Healthy', "Parkinson's"], help='Help text here')
        status = 1 if status == 'Healthy' else 0

    # Button to trigger prediction
    if st.button("Predict Parkinson's Disease"):
        inputs = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB,
                  APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        if any(input_field == '' for input_field in inputs):
            st.warning("Please fill in all the fields.")
            return

        user_input = [float(x) for x in inputs]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            st.success("The person has Parkinson's disease.")
            st.markdown("<a href='https://www.who.int/news-room/fact-sheets/detail/parkinson-disease#:~:text=Parkinson%20disease%20(PD)%20is%20a,muscle%20contractions%20and%20difficulty%20speaking.'>To know More about Parkinson</a>", unsafe_allow_html=True)

        else:
            st.success("The person does not have Parkinson's disease.")
            st.markdown("<a href='https://www.who.int/news-room/fact-sheets/detail/parkinson-disease#:~:text=Parkinson%20disease%20(PD)%20is%20a,muscle%20contractions%20and%20difficulty%20speaking.'>To know More about Parkinson</a>", unsafe_allow_html=True)

if __name__ == "__main__":
    parkinsons_model = None
    predict_parkinsons(parkinsons_model)
