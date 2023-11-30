# Python for Data Analysis
Final projet 2023 python for data analys

**our dataset :**
https://archive.ics.uci.edu/dataset/373/drug+consumption+quantified

**our team :**
- Tiberio Zolzettich
- Keziah Tabassomi

# Introduction

For this project, we analyzed data, did proccessing and modeling training. We based our work on an online data set. The dataset deals with the consumption of 19 legal and illegal drugs by 1,885 people around the world. They are the result of a survey in which participants were evaluated according to 12 criteria. Respondents were also asked about their use of substances such as cannabis, nicotine, cocaine, LSD or caffeine. They were asked to specify the last time they had used these substances, leading to the creation of 7 categories, ranging from "Never used" to "Used in the last day". The main subject of this project is to find out : 

**Which people are most at risk of taking drugs and what are the drugs that you are at risk to consume ?**

# Step 1 : Data pre-processing

We had to clean up the data in order to use it for data visualization and modeling. We did all the cleaning process in a notebook (APP/Notebooks/data_preproccessing.py). On the raw dataset (APP/Data/drug_consumption.data) we can see only numbers for each categories for exemple Male and Female are replace by -0.48246 and 0.48246. We create a mapping file (APP/Data/score_data.py) to replace all this values every time we want to show data vizualisation. We put columns name to each column, verify that there are not null values, replace the 7 drug consumption class (CL0 to CL6) by integer (0 to 6).

We create two new dataframe : 
- (APP/Data/df.csv) with the 7 class of drug consumption for some data visualization.
- (APP/Data/clean_df.csv) in this dataframe there are only two drug consumption class. "Never used" or "Used over a decade" are replaced by 0 (non consummer) and other class are replaced by 1 (consummer). This dataframe will simplify all the process for modeling and for evaluate your risk of being a drug consummer.

# Step 2 : Data visualization & Webapp



# Step 3 : Modeling

# API with FastAPI
