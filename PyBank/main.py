import os
import csv
import pandas as pd
import numpy as np
from pathlib import Path

file = Path('C:/Users/hahma/OneDrive/Desktop/PythonData/USCLOS201811DATA3/03_python/homework/Instructions/PyBank/Resources/budget_data.csv')

df_pd = pd.read_csv(file)

Total_Months = df_pd["Date"].count()

PLdiff = []

for i in range(Total_Months):
   PLdiff.append(df_pd["Profit/Losses"].iloc[i] - df_pd["Profit/Losses"].iloc[i-1])

df_pd.insert(2, "AvgChg", PLdiff)

PLdiff.pop(0)

Average_Change = round(sum(PLdiff)/(Total_Months-1), 2)
greatest_change = df_pd.iloc[df_pd['AvgChg'].idxmax()]
smallest_change = df_pd.iloc[df_pd['AvgChg'].idxmin()]

print("              ")
print("[Financial Analysis]")
print("----------------------")
print("    ", "Total Months in dataset equals: ", Total_Months)
print("    ", "Average Change between months equals: ", Average_Change)
print("    ", greatest_change["Date"], " was the date with the largest increase in profits at $" ,greatest_change["AvgChg"], ". Profits at this time were $", greatest_change["Profit/Losses"])
print("    ", smallest_change["Date"], " was the date with the largest decrease in profits at $" ,smallest_change["AvgChg"], ". Profits at this time were $", smallest_change["Profit/Losses"])
print("              ")

text = open('Financial Analysis.txt', "w")
print("              ",file=text)
print("[Financial Analysis]",file=text)
print("----------------------",file=text)
print("    ", "Total Months in dataset equals: ", Total_Months,file=text)
print("    ", "Average Change between months equals: ", Average_Change,file=text)
print("    ", greatest_change["Date"], " was the date with the largest increase in profits at $" ,greatest_change["AvgChg"], ". Profits at this time were $", greatest_change["Profit/Losses"],file=text)
print("    ", smallest_change["Date"], " was the date with the largest decrease in profits at $" ,smallest_change["AvgChg"], ". Profits at this time were $", smallest_change["Profit/Losses"],file=text)
print("              ",file=text)