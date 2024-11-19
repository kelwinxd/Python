import pandas as pd

basedata = pd.read_csv('Test2.csv')

X = basedata.iloc[:,:]

soma_test = basedata['Teste50'].sum()

print(soma_test)