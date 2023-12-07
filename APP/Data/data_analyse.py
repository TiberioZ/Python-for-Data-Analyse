from math import ceil
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

from APP.Data.mapping import Conversion


class DataAnalyse():

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.clean_df = pd.read_csv("C:/Users/tzolz/Desktop/PythonforDA/APP/Data/clean_df.csv")


    def barplot(self, column_name: str):
        df = self.df
        counts = df[column_name].value_counts()
        used = {
            0: "never used",
            1: "over a decade",
            2: "last decade",
            3: "last year",
            4: "last month",
            5: "last week",
            6: "last day"
        }
        counts.index = counts.index.map(used)
        df_counts = pd.DataFrame({'categories': counts.index, 'nb of people': counts.values})
        return df_counts

    def drug_distribution(self, name:str):
        df = self.df
        clean_df = self.clean_df
        drug_df = clean_df[clean_df[name]==1]

        conversion = Conversion()

        col1, col2 = st.columns(2,gap="large")

        #Age distribution barplot
        age_distribution = drug_df['Age'].value_counts()
        nb_age = df['Age'].value_counts()
        age = (age_distribution/nb_age)*100

        age_mapping = {
            -0.95197: '18-24',
            -0.07854: '25-34',
            0.49788: '35-44',
            1.09449: '45-54',
            1.82213: '55-64',
            2.59171: '65+'
        }
        age.index = age.index.map(age_mapping)
        df_counts = pd.DataFrame({'age': age.index, '% nb of people':age.values})
        col1.bar_chart(df_counts, x="age", y="% nb of people", color="#F63366", height=300)

        #Country distribution barplot
        country_distribution = drug_df['Country'].value_counts()
        nb_country = df['Country'].value_counts()
        country = (country_distribution/nb_country)*100
        country_mapping = {
            'Australia': -0.09765,
            'Canada': 0.24923,
            'New Zealand': -0.46841,
            'Other': -0.28519,
            'Republic of Ireland': 0.21128,
            'UK': 0.96082,
            'USA': -0.57009
        }
        inverse_country_mapping = {v: k for k, v in country_mapping.items()}
        country.index = country.index.map(inverse_country_mapping)
        df_country = pd.DataFrame({'country': country.index, '% nb of people':country.values})
        col1.bar_chart(df_country, x="country", y="% nb of people", color="#F63366", height=300)

        #Ethnicity distribution barplot
        eth_distribution = drug_df['Ethnicity'].value_counts()
        nb_eth = df['Ethnicity'].value_counts()
        eth = (eth_distribution/nb_eth)*100
        ethnicity_mapping = {
            'Asian': -0.50212,
            'Black': -1.10702,
            'Mixed-Black/Asian': 1.90725,
            'Mixed-White/Asian': 0.12600,
            'Mixed-White/Black': -0.22166,
            'Other': 0.11440,
            'White': -0.31685
        }
        inverse_eth_mapping = {v: k for k, v in ethnicity_mapping.items()}
        eth.index = eth.index.map(inverse_eth_mapping)
        df_eth = pd.DataFrame({'ethnicity': eth.index, '% nb of people':eth.values})
        col2.bar_chart(df_eth, x="ethnicity", y="% nb of people", color="#F63366", height=300)

        #Education distribution barplot
        edu_distribution = drug_df['Education'].value_counts()
        nb_edu = df['Education'].value_counts()
        edu = (edu_distribution/nb_edu)*100
        education_mapping = {
            'before 16 years': -2.43591,
            '16 years': -1.73790,
            '17 years': -1.43719,
            '18 years': -1.22751,
            'college or university': -0.61113,
            'diploma': -0.05921,
            'University': 0.45468,
            'Masters': 1.16365,
            'Doctorate': 1.98437
        }
        inverse_edu_mapping = {v: k for k, v in education_mapping.items()}
        edu.index = edu.index.map(inverse_edu_mapping)
        df_edu = pd.DataFrame({'left school': edu.index, '% nb of people':edu.values})
        col2.bar_chart(df_edu, x="left school", y="% nb of people", color="#F63366", height=300)