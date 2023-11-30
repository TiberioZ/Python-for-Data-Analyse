import streamlit as st
import subprocess
import sys
sys.path.append(r"C:\Users\tzolz\Desktop\PythonforDA")



st.set_page_config(
    page_title= "Project APP",
    page_icon= "💊"
)


st.title ("Drug consumption project")
st.subheader("Introduction")
st.markdown("")
st.markdown("""
Welcome to our webapp!

For this project, we analyzed data, did proccessing and modeling training. We based our work on an online data set. The dataset deals with the consumption of 19 legal and illegal drugs by 1,800 people around the world. The main subject of this project is to find out which people are most at risk of taking drugs.

""")
st.subheader("Analyse, train and modeling")
st.markdown("""

This webapp contains two pages:
- **training statistics:** On this page you'll find graphical representations of the dataset analyzed, with several barplots to help you understand which population is most at risk of taking which drug.
- **Evaluate your risk:** On this page, you can test your data to see which drugs you are most likely to use (for prevention purposes).
            
The results on the second page are calculated using "logistic regression" modeling, which we found to be the most accurate model in our case. 

**Possible improvements for greater precision:** retrieve the test results and ask the person whether the result is good for each drug, so as to be able to improve the model with weightings on the different data.
""")

