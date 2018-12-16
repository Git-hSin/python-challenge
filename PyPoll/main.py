import os
import csv
import pandas as pd
import numpy as np
from pathlib import Path

file = Path('C:/Users/hahma/OneDrive/Desktop/PythonData/USCLOS201811DATA3/03_python/homework/Instructions/PyPoll/Resources/election_data.csv')

df_pd = pd.read_csv(file)


df_pd1 = pd.DataFrame(df_pd["Candidate"].value_counts())

total = df_pd1["Candidate"].sum()

text = open('PollStats.txt', "w")
print(df_pd1["Candidate"], df_pd1["Candidate"]/total, "Winner: Khan",file=text)
