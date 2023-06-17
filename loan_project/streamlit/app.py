import streamlit as st
import requests

import numpy as np
import pandas as pd

# CSS = """
# .css-ffhzg2 {
#     background = rgb(38, 62, 111);
# }

# """

if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html = True)


st.markdown(
"""# Credit Approval Simulation
## Check your loan conditions based on your personal information.

The goal of this project is to provide information to lenders and users that are searching for a loan.

We provide a prediction on whether your loan application would be successful and an estimation of your probable interest rate.
"""
)

# Tem como limitar valores mínimos e máximos?
# loan_amnt
amount = st.number_input('How much do you wish to borrow?')
st.write("The amount you want is ", amount)

# annual_inc
income = st.number_input('What is your approximate annual income?')
st.write("Your annual income is ", income)

# tot_cur_bal
balance = st.number_input('Provide an estimation of how much money you have as assets and at your disposal.')
st.write("Your approximate balance and assets are ", balance)


# Categorical variables
df = pd.read_csv('../raw_data/treated_df.csv')

# term
possible_terms = np.sort(df['term'].unique())
term = st.selectbox('Select the term of your loan:', possible_terms)
st.write('The term select is ', term)

# grade
possible_grades = np.sort(df['grade'].unique())
grade = st.selectbox('Select your credit grade: ', possible_grades)
st.write('Your credit grade is ', grade)

# emp_length
possible_emp = np.sort(df['emp_length'].unique())
emp_length = st.selectbox('What is your employment status: ', possible_emp)
st.write('Your employment status is ', emp_length)

# home_onwership
possible_home = np.sort(df['home_ownership'].unique())
home_ownership = st.selectbox('What is your home ownership status: ', possible_home)
st.write("You've selected ", home_ownership)

# purpose
possible_purpose = np.sort(df['purpose'].unique())
purpose = st.selectbox('What will this loan be destined for: ', possible_purpose)
st.write("You've selected ", purpose)

# Getting features from user
dict_to_api = {
    'loan_amnt': amount,
    'annual_inc': income,
    'tot_cur_bal': balance,
    'term': term,
    'grade': grade,
    'emp_lengt': emp_length,
    'home_ownership': home_ownership,
    'purpose': purpose
}

# Sending to API
st.write(dict_to_api)
st.write("Confirm your information then press the button below to get your results.")

if st.button('Make My Prediction'):
    print("Processando seus dados")

    # Call da api
    res = requests.get('http://127.0.0.1:5000/predict', params=dict_to_api)
    st.write(res.json())

    st.write('Aqui esta sua call de api:')
else:
    st.write('Aguardando envio de informacoes')
