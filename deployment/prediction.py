import streamlit as st
import pandas as pd
import pickle
from PIL import Image

def run():
    # buat header
    st.header("Welcome to the Prediction page!")

    # Description
    st.write("This is the model evaluation section.")
    st.write("This study used ROC-AUC Curve and F1-score to evaluate the model's performance. Among the classification models used, logistic regression performed best.")

    # Load image
    st.write('\n')
    roc_auc_pict = Image.open('ROC-AUC Curve Results.png')
    st.image(roc_auc_pict, width=300, use_column_width='always')
    st.write("The Accuracy = 84%, F1-score = 54%.")

    st.write("Please input customer's credit status information to predict the decision for default payment on October 2005.")

    # load model yang sudah disave
    with open('model_log.pkl','rb') as file_1:
        my_model = pickle.load(file_1)

    with open('model_scaler.pkl', 'rb') as file_2:
        sc= pickle.load(file_2)

    # semua fitur yang masuk dalam modelling harus ditulis
    with st.form("Input informasi nasabah"):
        sex = st.radio('Gender: [1 = Male, 2= Female]', ['1', '2'])
        education_level = st.selectbox('Education Level: [1 = graduate school, 2 = university, 3 = high school, 4 = others, 5 = unknown, 6 = unknown]',['1','2','3','4','5','6'])
        marital_status = st.selectbox('Marital Status: [1 = married, 2 = single, 3 = others]',['1', '2', '3'])
        limit_balance = st.slider('Balance Limit', min_value = 10000,max_value = 1000000,help='limit_balance')
        pay_0 = st.slider('Repayment status in September 2005. [-2,0 = unknown,-1 = pay duly, 1 = payment late 1 month, 2 = payment late 2 months]',min_value = -2, max_value = 7,step =1)
        pay_2 = st.slider('Repayment status in August 2005. Input values are the same as that in September 2005.',min_value = -2, max_value = 7,step =1)
        pay_3 = st.slider('Repayment status in July 2005. Input values are the same as that in September 2005.',min_value = -2, max_value = 7,step =1)
        pay_4 = st.slider('Repayment status in June 2005. Input values are the same as that in September 2005.',min_value = -2, max_value = 7,step =1)
        pay_5 = st.slider('Repayment status in May 2005. Input values are the same as that in September 2005.',min_value = -2, max_value = 7,step =1)
        pay_6 = st.slider('Repayment status in April 2005. Input values are the same as that in September 2005.',min_value = -2, max_value = 7,step =1)
        bill_amt_1 = st.slider('Amount of bill statement in September, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        bill_amt_2 = st.slider('Amount of bill statement in August, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        bill_amt_3 = st.slider('Amount of bill statement in July, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        bill_amt_4 = st.slider('Amount of bill statement in June, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        bill_amt_5 = st.slider('Amount of bill statement in May, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        bill_amt_6 = st.slider('Amount of bill statement in April, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        pay_amt_1 = st.slider('Amount of previous payment in September, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        pay_amt_2 = st.slider('Amount of previous payment in August, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        pay_amt_3 = st.slider('Amount of previous payment in July, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        pay_amt_4 = st.slider('Amount of previous payment in June, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        pay_amt_5 = st.slider('Amount of previous payment in May, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        pay_amt_6 = st.slider('Amount of previous payment in April, 2005 (NT dollar).',min_value = 0, max_value = 500000)
        # default_payment_next_month = st.slider('default_payment_next_month',min_value = 0, max_value = 1,step =1)
        # submit form
        sub = st.form_submit_button('Predict')

    if sub:
        data_predict = {'sex': sex,'education_level': education_level,'marital_status':marital_status,'limit_balance':limit_balance,'pay_0':pay_0,'pay_2':pay_2,'pay_3':pay_3,'pay_4':pay_4,'pay_5':pay_5,'pay_6':pay_6,'bill_amt_1':bill_amt_1,'bill_amt_2':bill_amt_2,'bill_amt_3':bill_amt_3,'bill_amt_4':bill_amt_4,'bill_amt_5':bill_amt_5,'bill_amt_6':bill_amt_6,'pay_amt_1':pay_amt_1,'pay_amt_2':pay_amt_2,'pay_amt_3':pay_amt_3,'pay_amt_4':pay_amt_4,'pay_amt_5':pay_amt_5,'pay_amt_6':pay_amt_6}
        data = pd.DataFrame([data_predict])
        st.write("#### Hasil input data:")
        st.dataframe(data)
        try:
            data_scaled = sc.transform(data)
            y_pred = my_model.predict(data_scaled)
            st.write('Prediction about default client (1) or non-default (0) is: ', y_pred[0])
        except Exception as e:
            st.error(f'An error occured:{e}')
if __name__ == '__main__':
    run()
