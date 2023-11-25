import streamlit as st

st.title("Evaluate your risk of being a drug consumer")
st.markdown("Fill all the option in this page and click on the button at the end to see your results")

col1, col2= st.columns(2)

with col1:
    st.selectbox("Age",["18-24", "25-34", "35-44","45-54","55-64","65+"])
    st.selectbox(
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
    st.selectbox("Gender",["Female", "Male"])
    st.selectbox(
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
    
st.selectbox(
        "Education",
            [
                "Left school before 16 years",
                "Left school at 16 years",
                "Left school at 17 years",
                "Left school at 18 years",
                "Some college or university, no certificate or degree",
                "Professional certificate / diploma",
                "University degree",
                "Masters degree",
                "Doctorate degree"
            ]
    )

st.write(" ")
st.write("Use the sliders to indicate your level for each categorie")

st.slider("**Neuroticism :** Tendency to feel negative emotions, anxiety.",min_value=12, max_value=60,)
st.slider("**Extraversion :** the term refers to a state of being where someone “recharges,” or draws energy, from being with other people.",min_value=16, max_value=59)
st.slider("**Openness to experience :** a sense of curiosity, open-mindedness, and acceptance of novel experiences.",min_value=24, max_value=60)
st.slider("**Agreeableness :** a person's ability to put others needs before their own.",min_value=12, max_value=60)
st.slider("**Conscientiousness :** Conscientiousness is the personality trait of being careful or diligent",min_value=17, max_value=59)
st.slider("**Impulsiveness :** behaving without thinking and without realizing the risk involved in the behavior.",min_value=0, max_value=10)
st.slider("**Sensation seeking :**  the tendency to pursue new and different sensations, feelings, and experiences.",min_value=0, max_value=11)

st.write(" ")
st.button("Check results", type = "primary", use_container_width = True)
    


