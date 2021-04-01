import streamlit as st
import pandas as pd
import xlrd


df = pd.read_excel(r"E:\DS\test_excel\test_excel.xlsx")

st.write("""
# Inofrmation of Request by MCH
""")
st.sidebar.header('Please choose your Request Number')

def user_input_features():
    display = df['request#']
    value=st.sidebar.selectbox("vendor name", display)

    data=df[df['request#']==value]
    st.write("""
    ## ** This is  {}** 
    """.format(value))
    st.write('Line Number is ',len(data))
    st.write('Total number is ',sum(data['request#']))
    return data
df2 = user_input_features()

st.subheader('User Input parameters')
st.write(df2)

