from math import ceil
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\tzolz\Desktop\PythonforDA\APP\Data\clean_df.csv", sep=',')

def barplot(column_name: str, ax):
    sns.countplot(x=column_name, data=df, order=['CL0', 'CL1', 'CL2', 'CL3', 'CL4', 'CL5', 'CL6'], ax=ax,)
    ax.set_ylim(0, 1500)
    return ax


df_barplot = df.iloc[:, 13:32]
plot_list = []

nb_cols = len(df_barplot.columns)
num_cols = 4
num_rows = ceil(nb_cols/4)
fig, axs = plt.subplots(num_rows, num_cols)

# Iterate over columns and create count plots
for i, column in enumerate(df_barplot.columns):
    ax = axs[i] if num_rows == 1 else axs[i // num_cols, i % num_cols]
    plot_list.append(barplot(column, ax))

# Hide any remaining empty subplots
for i in range(len(df_barplot.columns), num_cols * num_rows):
    axs.flatten()[i].axis('off')


fig.show()






