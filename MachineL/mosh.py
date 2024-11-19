import pandas as pd
import os

print(os.path.exists("vgsales.csv"))

df = pd.read_csv("vgsales.csv")

print(df.describe())