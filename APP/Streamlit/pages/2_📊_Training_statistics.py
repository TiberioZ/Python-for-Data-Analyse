from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
import sys
import numpy as np
sys.path.append(r"C:\Users\tzolz\Desktop\PythonforDA")

from APP.Data.data_analyse import DataAnalyse


analyse = DataAnalyse(r"C:\Users\tzolz\Desktop\PythonforDA\APP\Data\df.csv")

st.set_page_config(
    page_title= "Project APP",
    page_icon= "💊"
)

st.title ("All the statistics about the training data")
st.markdown("")
st.subheader("I. Distribution of people according to the last time they used each drug")
st.markdown("")


columns_name = [
    'Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Caffeine', 'Cannabis', 'Chocolate',
    'Coke', 'Crack', 'Ecstasy', 'Heroin', 'Ketamine', 'Legalh', 'LSD', 'Meth',
    'Mushrooms', 'Nicotine', 'Semer', 'VSA'
]

def create_bar_chart(substance, col):
    # Assuming 'analyse' is the DataFrame you're working with
    substance_data = analyse.barplot(substance)
    col.markdown(f"<p style='text-align: center;'>{substance}</p>", unsafe_allow_html=True)
    col.bar_chart(substance_data, x="categories", y="nb of people", color="#F63366", height=200)



col1, col2, col3 = st.columns(3)

# Counter variable to distribute charts among columns
counter = 0

for substance in columns_name:
    if counter % 3 == 0:
        create_bar_chart(substance, col1)
    elif counter % 3 == 1:
        create_bar_chart(substance, col2)
    else:
        create_bar_chart(substance, col3)
    
    counter += 1


st.markdown("")
st.subheader("II. Percentage of people by category using this drug")
st.markdown("")

drug_selected = st.selectbox("Drug",['Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Caffeine', 'Cannabis', 'Chocolate',
            'Coke', 'Crack', 'Ecstasy', 'Heroin', 'Ketamine', 'Legalh', 'LSD', 'Meth',
            'Mushrooms', 'Nicotine', 'Semer', 'VSA'])

st.markdown("")
analyse.drug_distribution(drug_selected)







    