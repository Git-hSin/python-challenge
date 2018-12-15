import os
import csv
import pandas as pd
from pathlib import Path

file = Path('C:/Users/hahma/OneDrive/Desktop/PythonData/USCLOS201811DATA3/03_python/homework/Instructions/PyBank/Resources/budget_data.csv')

df_pd = pd.read_csv(file)

Total_Months = df_pd["Date"].count()

PLdiff = []

for i in range(Total_Months):
   PLdiff.append(df_pd["Profit/Losses"].iloc[i] - df_pd["Profit/Losses"].iloc[i-1])

PLdiff.pop(0)

Average_Change = sum(PLdiff)/(Total_Months-1)

print(Average_Change)