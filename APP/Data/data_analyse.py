from math import ceil
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt


class DataAnalyse():

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)


    def barplot(self, column_name: str):
        df = self.df
        counts = df[column_name].value_counts()
        df_counts = pd.DataFrame({'categories': counts.index, 'nb of people': counts.values})
        return df_counts



