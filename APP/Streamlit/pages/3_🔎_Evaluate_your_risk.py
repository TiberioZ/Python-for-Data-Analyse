import time
import pandas as pd
import streamlit as st

from APP.Data.machine_learning import MachineLearning
from APP.Data.score_data import Conversion

ml_instance = MachineLearning(r"C:\Users\tzolz\Desktop\PythonforDA\APP\Data\clean_df.csv")
convert = Conversion()

st.set_page_config(
    page_title= "Project APP",
    page_icon= "💊"
)

st.title("Evaluate your risk of being a drug consumer")
st.markdown("Fill all the option in this page and click on the button at the end to see your results")

col1, col2= st.columns(2)

with col1:
    age = st.selectbox("Age",["18-24", "25-34", "35-44","45-54","55-64","65+"])
    country = st.selectbox(
        "Country",
        [
            "Australia",
            "Canada",
            "New Zealand",
            "Other",
            "Republic of Ireland",
            "UK",
            "USA",
        ]
    )
    

with col2:
    gender = st.selectbox("Gender",["Female", "Male"])
    ethnicity = st.selectbox(
        "Ethnicity",
        [
            "Asian",
            "Black",
            "Mixed-Black/Asian",
            "Mixed-White/Asian",
            "Mixed-White/Black",
            "Other",
            "White",
        ]
    )
    
education = st.selectbox(
        "Education",
            [
                "Left school before 16 years",
                "Left school at 16 years",
                "Left school at 17 years",
                "Left school at 18 years",
                "Some college or university, no certificate or degree",
                "Professional certificate/diploma",
                "University degree",
                "Masters degree",
                "Doctorate degree"
            ]
    )

st.write(" ")
st.write("Use the sliders to indicate your level for each categorie")

nscore = st.slider("**Neuroticism :** Tendency to feel negative emotions, anxiety.",min_value=12, max_value=60,)
escore = st.slider("**Extraversion :** the term refers to a state of being where someone “recharges,” or draws energy, from being with other people.",min_value=16, max_value=59)
oscore = st.slider("**Openness to experience :** a sense of curiosity, open-mindedness, and acceptance of novel experiences.",min_value=24, max_value=60)
ascore = st.slider("**Agreeableness :** a person's ability to put others needs before their own.",min_value=12, max_value=60)
cscore = st.slider("**Conscientiousness :** Conscientiousness is the personality trait of being careful or diligent",min_value=17, max_value=59)
impulsive = st.slider("**Impulsiveness :** behaving without thinking and without realizing the risk involved in the behavior.",min_value=1, max_value=10)
ss = st.slider("**Sensation seeking :**  the tendency to pursue new and different sensations, feelings, and experiences.",min_value=1, max_value=11)


st.write(" ")
if st.button("Check results", type = "primary", use_container_width = True):

    #progress bar
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    age_str = str(age)
    gender_str = str(gender)
    education_str = str(education)
    country_str = str(country)
    ethnicity_str = str(ethnicity)
    user_data = {
        'Age': [convert.get_value_from_age_group(age_str)],
        'Gender': [convert.get_value_from_gender(gender_str)],  
        'Education': [convert.get_education_value(education_str)],  
        'Country': [convert.get_country_value(country_str)],  
        'Ethnicity': [convert.get_ethnicity_value(ethnicity_str)],  
        'Nscore': [convert.get_nscore_value(nscore)],
        'Escore': [convert.get_escore_value(escore)],
        'Oscore': [convert.get_oscore_value(oscore)],
        'Ascore': [convert.convert_ascore_to_value(ascore)],
        'Cscore': [convert.convert_value_to_cscore(cscore)],
        'Impulsive': [convert.convert_to_impulsiveness(impulsive)],
        'SS': [convert.convert_to_sensation_seeking(ss)]
        }

    user_df = pd.DataFrame(user_data)
    result = ml_instance.dataframe_prediction_drugs(user_df)

    result = result.replace({0: 'low risk', 1: 'high risk'})
   
    def style_cells(value):
        style = 'font-weight: bold; text-align: center;'
        
        if 'high risk' in value.lower():
            color = 'red'
        elif 'low risk' in value.lower():
            color = 'green'
        else:
            color = 'black'
        
        return f'background-color: {color}; {style}'

    # Apply the styling function to the DataFrame
    styled_df = result.style.applymap(style_cells)

    # Display the styled DataFrame in Streamlit
    st.dataframe(styled_df, hide_index=True)

    st.write("⚠️ **High risk** represents individuals who have used drugs at least once in the past 10 years.")
    st.write("✅ **Low risk** represents individuals who used this drug more than 10 years ago or have never used it.")
