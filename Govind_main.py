import os
import pickle
import streamlit as st
# from keras.models import load_model
from streamlit_option_menu import option_menu
from Govind_Diabetes import predict_diabetes
# from Govind_Heart import predict_heart
# from Govind_Lungs import predict_lung_cancer
# from Govind_Parkinson import predict_parkinsons
# from Govind_Kidney import predict_kidney_disease
from Govind_Home import welcome

from Govind_footer import show_footer
from Govind_nav_for_all_page import NavForAll

# Display the dataset using Streamlit
st.title("Diabetes Prediction App")
st.subheader("Diabetes Dataset")
st.dataframe(diabetes_dataset)

# Summary statistics
st.subheader("Dataset Summary")
st.write(diabetes_dataset.describe())

# Class distribution
st.subheader("Class Distribution")
st.write(diabetes_dataset['Outcome'].value_counts())

# Mean values by Outcome
st.subheader("Mean Values by Outcome")
st.write(diabetes_dataset.groupby('Outcome').mean())


# Set page configuration
st.set_page_config(page_title="HealthReportAnalyzer",
                   layout="wide",
                   page_icon="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcR8Rnwxuw0fvA1xuuvvBpAz97AQSqdwR5pp2BfvLl5kkanrXXkq")

# Function to create navigation bar
NavForAll()

# Sidebar for navigation
with st.sidebar:
    # Get the directory of the main script
    main_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the logo image
    logo_path = os.path.join(main_dir, "Plaksha Logo.png")
    # Insert Plaksha Logo image
    st.image(logo_path, width=50, use_column_width=False, output_format="PNG")

    # Apply circular shape to the image using CSS
    st.markdown("""
    <style>
    /* Apply circular shape to the image */
    .sidebar .stImage > img {
        border-radius: 50%;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # # Create a clickable link for the "Mini Doctor" option
    # selected = option_menu('Choose Disease Prediction Model',
    #                        ['Home','Diabetes Prediction',
    #                         'Heart Disease Prediction',
    #                         'Lungs Cancer Prediction',
    #                         'Kidney Disease Prediction',
    #                         'Parkinsons Prediction',],
    #                        menu_icon='hospital-fill',
    #                        icons=['person','activity','heart','lungs', 'activity','activity'],
    #                        default_index=0)

    # Create a clickable link for the "Mini Doctor" option
    selected = option_menu('Choose Disease Prediction Model',
                           ['Home','Diabetes Prediction'],
                           menu_icon='hospital-fill',
                           icons=['person','activity','heart','lungs', 'activity','activity'],
                           default_index=0)

# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
# heart_disease_model = pickle.load(open(f'{main_dir}/saved_models/heart_disease_model.sav', 'rb'))
# parkinsons_model = pickle.load(open(f'{main_dir}/saved_models/parkinsons_model.sav', 'rb'))
# lung_cancer_model = pickle.load(open(f'{main_dir}/saved_models/Lung_cancer_prediction.sav', 'rb'))
# # kidney_model = pickle.load(open(f'{main_dir}/saved_models/kidney_disease_prediction.sav', 'rb'))
# kidney_model = load_model(f'{main_dir}/saved_models/kidney_disease_prediction.h5')

# Main Streamlit code
if selected == "Home":
    welcome()
elif selected == 'Diabetes Prediction':
    predict_diabetes(diabetes_model)
# elif selected == 'Heart Disease Prediction':
#     predict_heart(heart_disease_model)
# elif selected == 'Parkinsons Prediction':
#     predict_parkinsons(parkinsons_model)
# elif selected == 'Lungs Cancer Prediction':
#     predict_lung_cancer(lung_cancer_model)
# elif selected == 'Kidney Disease Prediction':
#     predict_kidney_disease(kidney_model)

# Footer
show_footer()
