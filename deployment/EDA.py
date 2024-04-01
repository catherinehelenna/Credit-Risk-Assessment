import streamlit as st
import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.header("Welcome to Data Analysis page!")
    st.write("Here is a simple Exploratory Data Analysis study, followed by relevant visualizations.")

    # import visualisasi
    main_data = pd.read_csv('client_data.csv')

    st.write("\n")
    st.write("##### 1. The dataset used in this study")
    st.write("The table below shows the columns of information that will be used to predict default_payment_next_month. Because the machine learning algorithm used is logistic regression, the default_payment_next_month data is needed for training as the target variable. There are two types of data in default_payment_next_month: 1 means default, while 0 means no default.")
    st.dataframe(main_data)

    # untuk boxplot
    data = {'sex': main_data['sex'], 'limit_balance':main_data['limit_balance']}
    variasi_harga = pd.DataFrame(data).reset_index(drop=True)

    # menambah kolom baru untuk konversi ke string dari angka
    variasi_harga.insert(1,'new_sex','no values')
    variasi_harga.loc[variasi_harga['sex'] == 1,'new_sex'] = 'Male'
    variasi_harga.loc[variasi_harga['sex'] == 2,'new_sex'] = 'Female'


    # statistika deskriptif limit_balance berdasarkan gender
    variasi_harga.groupby('new_sex')['limit_balance'].describe()

    # make a box plot
    fig = plt.figure(figsize=(15,5))
    sns.boxplot(x='new_sex',y='limit_balance', hue='new_sex',data=variasi_harga)

    # memberikan label
    plt.xlabel('Gender')
    plt.ylabel('Limit Balance')
    plt.title('Box Plot of Limit Balance Variation based on Gender')

    st.write("\n")
    st.write("##### 2. Variation of Credit Card Limit by Gender")
    st.write("Upon a general overview of the box plot results, the variation of limit_balance for male and female customers appears quite similar. However, there are more female customers with high limit_balance compared to males due to a higher number of outliers. Based on the results of the ANOVA test, it is found that the difference in limit_balance is influenced by the gender type.")
    # Displaying the plot
    st.pyplot(fig)


    # untuk visualisasi dengan bar graph
    # membuat dataframe baru
    customer_gender = pd.DataFrame(main_data.groupby('sex')['sex'].value_counts().reset_index())

    # mengubah nilai angka pada sex (gender) menjadi string
    customer_gender['sex'] = customer_gender['sex'].replace(1,'Male')
    customer_gender['sex'] = customer_gender['sex'].replace(2,'Female')

    # mengubah nama label dari count => number_of_customers
    customer_gender.rename(columns={'count':'number_of_customers'},inplace = True)

    # mendefinisikan values x dan y
    x_values = customer_gender['sex']
    y_values = customer_gender['number_of_customers']

    # Definisikan warna berdasarkan gender
    colors = ['lightblue' if s == 'Male' else 'pink' for s in customer_gender['sex']]

    # plotting dengan bar graph
    # make a box plot
    fig2 = plt.figure(figsize=(15,5))
    plt.bar(x_values,y_values,color=colors)

    # menambahkan label pada axisnya
    plt.xlabel('Gender')
    plt.ylabel('Number of Customers')
    plt.title('Number of Customers for Each Gender')

    st.write("\n")
    st.write("##### 3. Number of Credit Card Users by Gender")
    st.write("As seen in the bar graph below, the number of female customers is also higher than male customers.")
    # Displaying the plot
    st.pyplot(fig2)

if __name__ == '__main__':
    run()