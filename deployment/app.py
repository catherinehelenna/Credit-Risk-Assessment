import streamlit as st
import prediction
import EDA
from PIL import Image

page = st.sidebar.selectbox(label= 'Select Menu: ', options=['Home','Data Analysis','Predict Default Decision'])
    
if page == 'Home':
    st.header("CreditGuide: Your Trustworthy Defaulter Detector")
    st.write("\n")
    st.write("Your most trustworthy default detector webapp is at your service. Using the clients' credit payment information since April to September 2005, we have developed a prototype for predicting default clients on the following month (October 2005).")
    st.write("Please go to the sidebar for checking the features available in this web-app.")
    # Display the image as a watermark
    # Load your image
    img = 'creditguide_logo.png'
    st.image(img, width=300, use_column_width='always')

elif page == 'Data Analysis':
    EDA.run()
else:
    prediction.run()