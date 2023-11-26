import json
from typing import Union
from fastapi import APIRouter, FastAPI
import numpy as np
import pandas as pd
from pydantic import BaseModel
import sys

from APP.Data.score_data import Conversion
sys.path.append(r'C:/Users/tzolz/Desktop/PythonforDA')

from APP.API.basemodels import Result, User
from APP.Data.machine_learning import MachineLearning

ml = MachineLearning(r"C:\Users\tzolz\Desktop\PythonforDA\APP\Data\clean_df.csv")
convert = Conversion()

router = APIRouter(
    prefix ="/drugrisk",
    tags = ["Evaluate risk of drug consumption"]
)


# Result for all drugs
@router.get("",
            description="0 represents **low risk** \n1 represents **high risk**"
            )
def get_the_result_for_all_drugs(item: User):
    user_data = {
        'Age': [convert.get_value_from_age_group(item.Age)],
        'Gender': [convert.get_value_from_gender(item.Gender)],  
        'Education': [convert.get_education_value(item.Education)],  
        'Country': [convert.get_country_value(item.Country)],  
        'Ethnicity': [convert.get_ethnicity_value(item.Ethnicity)],  
        'Nscore': [convert.get_nscore_value(item.Nscore)],
        'Escore': [convert.get_escore_value(item.Escore)],
        'Oscore': [convert.get_oscore_value(item.Oscore)],
        'Ascore': [convert.convert_ascore_to_value(item.Ascore)],
        'Cscore': [convert.convert_value_to_cscore(item.Cscore)],
        'Impulsive': [convert.convert_to_impulsiveness(item.Impulsive)],
        'SS': [convert.convert_to_sensation_seeking(item.SS)]
        }

    user_df = pd.DataFrame(user_data)
    response = ml.prediction_drugs(user_df)
    
    rp = Result(
        Alcohol=response['Alcohol'],
        Amphet= response['Amphet'],
        Amyl= response['Amyl'],
        Benzos= response['Benzos'],
        Caffeine= response['Caffeine'],
        Cannabis= response['Cannabis'],
        Chocolate= response['Chocolate'],
        Coke= response['Coke'],
        Crack= response['Crack'],
        Ecstasy= response['Ecstasy'],
        Heroin= response['Heroin'],
        Ketamine= response['Ketamine'],
        Legalh= response['Legalh'],
        LSD= response['LSD'],
        Meth= response['Meth'],
        Mushrooms= response['Mushrooms'],
        Nicotine= response['Nicotine'],
        Semer= response['Semer'],
        VSA= response['VSA']
    )
    
    return rp



# Result for une drug filtered in params
@router.get(
            "/{drug}",
            description="0 represents **low risk** \n1 represents **high risk**"
        )
def get_the_result_of_one_drug(drug: str, item: User):
    user_data = {
        'Age': [convert.get_value_from_age_group(item.Age)],
        'Gender': [convert.get_value_from_gender(item.Gender)],  
        'Education': [convert.get_education_value(item.Education)],  
        'Country': [convert.get_country_value(item.Country)],  
        'Ethnicity': [convert.get_ethnicity_value(item.Ethnicity)],  
        'Nscore': [convert.get_nscore_value(item.Nscore)],
        'Escore': [convert.get_escore_value(item.Escore)],
        'Oscore': [convert.get_oscore_value(item.Oscore)],
        'Ascore': [convert.convert_ascore_to_value(item.Ascore)],
        'Cscore': [convert.convert_value_to_cscore(item.Cscore)],
        'Impulsive': [convert.convert_to_impulsiveness(item.Impulsive)],
        'SS': [convert.convert_to_sensation_seeking(item.SS)]
        }

    user_df = pd.DataFrame(user_data)
    response = ml.prediction_one_drug(user_df, drug_name=drug)
    
    result = {
        drug : str(response[drug])
    }

    return result