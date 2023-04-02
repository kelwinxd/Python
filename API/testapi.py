import requests
import json

# https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
moeda = input("What current? ")
cotacao_dolar = cotacoes[f"{moeda}"]["bid"]


print(cotacao_dolar)
