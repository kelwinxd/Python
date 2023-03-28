import pandas

tabela = pandas.read_csv(r"C:\Users\Kelwin\Downloads\teste.csv", sep=";")



total_gasto = tabela["ValorFinal"]
    



print(total_gasto)