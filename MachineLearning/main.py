import numpy as np
import pandas as pd



baseData = pd.read_csv('test.csv', delimiter=",", header=None, skipinitialspace=True)
baseData = baseData.dropna(axis=1, how='all')
X = baseData.values

print(X)