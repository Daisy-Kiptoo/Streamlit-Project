import streamlit as st
import pickle
import streamlit_option_menu
from streamlit_option_menu import option_menu

# loading the saved model
heart_model = pickle.load(open('heart_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    select = option_menu('Heart Disease Prediction System',
                         
                         ['Heart Disease Prediction',
                          'Insert CSV File'],
                         
                         icons = ['heart', 'filetype-csv'],
                         default_index = 0)
    
# Heart Disease Prediction page
if (select == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction using ML')
    
    # getting the input data from the user
    # columns for the input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest pain type')
    
    with col1:
        trestbps = st.text_input('Resting blood pressure')
        
    with col2:
        chol = st.text_input('Serum cholestoral')
        
    with col3:
        fbs = st.text_input('Fasting blood pressure')
    
    with col1:
        restecg = st.text_input('Resting electrocardiographic results')
    
    with col2:
        thalach = st.text_input('Maximum heart rate achieved')
    
    with col3:
        exang = st.text_input('Exercise induced angina')
    
    with col1:
        oldpeak = st.text_input('Oldpeak')
    
    with col2:
        slope = st.text_input('The slope of the peak exercise')
    
    with col3:
        ca = st.text_input('The number of major vessels')
    
    with col1:
        thal = st.text_input('Thal')
    
    # prediction code
    heart_dis_diag = ''
    
    # create a button for prediction
    if st.button('Heart Disease Heart Results'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0] == 0):
            heart_dis_diag = 'The patient does NOT have heart disease.'
        else:
            heart_dis_diag = 'The patient has heart disease.'
            
    st.success(heart_dis_diag)

if (select == 'Insert CSV File'):
    # page title
    st.title('Insert CSV File')
    
    
