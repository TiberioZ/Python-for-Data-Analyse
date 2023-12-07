# Python for Data Analysis
Final Project 2023: Python for Data Analysis

**Dataset:**
https://archive.ics.uci.edu/dataset/373/drug+consumption+quantified

**Team Members:**

- Tiberio Zolzettich
- Keziah Tabassomi

### Introduction

In this project, we conducted an analysis of data, performed processing, and undertook modeling training using an online dataset. The dataset involves the consumption of 19 legal and illegal drugs by 1,885 individuals globally, evaluated through 12 criteria in a survey. Participants were questioned about their usage of substances such as cannabis, nicotine, cocaine, LSD, or caffeine, providing information on the last time they consumed these substances, resulting in the creation of 7 categories ranging from "Never used" to "Used in the last day." The primary objective of this project is to determine:

**Which population is most susceptible to drug consumption for each drug, and which drugs pose the highest risk of consumption based on your personal data?**

### Data Pre-processing, Visualization, and Modeling

To prepare the data for visualization and modeling, we performed cleaning operations detailed in the notebook (data_preprocessing.py). In the raw dataset (drug_consumption.data), numerical values were used for each category; for instance, Male and Female were replaced by -0.48246 and 0.48246. A mapping file (score_data.py) was created to replace these values during data visualization. We assigned column names, checked for null values, and replaced the 7 drug consumption classes (CL0 to CL6) with integers (0 to 6).

Two new dataframes were generated:

(APP/Data/df.csv) containing the 7 drug consumption classes for data visualization.
(APP/Data/clean_df.csv) with only two drug consumption classes: "Never used" or "Used over a decade" replaced by 0 (non-consumer), and other classes replaced by 1 (consumer). This dataframe simplifies the modeling process and risk evaluation for drug consumption.
Data visualization can be observed on the Streamlit web app, showcasing various bar plots representing the distribution of drug consumption.

After reviewing the data visualization, we experimented with different models to identify the best fit for this project. The optimal model for this dataframe is "logistic regression," a classification model. With this model's training, we can assess the risk of an individual being a drug consumer based on the provided 12 criteria.

**Possible improvements for greater precision:** retrieve the test results and ask the person whether the result is good for each drug, so as to be able to improve the model with weightings on the different data.

### Execution

#### Streamlit Web App

To run this project, follow these steps:

  1. Clone the Git repository.
  2. Install the required dependencies via pip install -r requirements.txt.
  3. Execute in the terminal "Streamlit run {absolute path of 1_👋_Welcome.py}"

#### API by FastAPI

To run the API of this project, follow these steps:

  1. Clone the Git repository.
  2. Install the required dependencies via pip install -r requirements.txt.
  3. Run the main.py file.
  4. Open http://127.0.0.1:5000/docs for the API documentation.
     
### Tools

- Python files & notebooks
- Libraries: Pandas, NumPy, Scikit-Learn, Matplotlib, etc.
- Streamlit (WebApp)
- FastApi (API)
