import streamlit as st
import pandas as pd

st.write("""
# My firt app!
""")

column_names = ['ID',
                'Age', 
                'Gender', 
                'Education', 
                'Country', 
                'Ethnicy', 
                'Nscore', 
                'Escore', 
                'Oscore', 
                'Ascore', 
                'Cscore', 
                'Impulsive', 
                'SS', 
                'Alcohol', 
                'Amphet', 
                'Amyl', 
                'Benzos', 
                'Caff', 
                'Cannabis', 
                'Choc',
                'Coke',
                'Crack',
                'Ecstasy',
                'Heroin',
                'Ketamine',
                'Legalh',
                'LSD',
                'Meth',
                'Mushrooms',
                'Nicotine',
                'Semer',
                'VSA']

df = pd.read_csv(r"C:\Users\tzolz\Desktop\PythonforDA\DATA\drug_consumption.data", sep=',', index_col=0, names=column_names)
st.line_chart(df['Age'])

