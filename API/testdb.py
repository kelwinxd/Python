import requests




value1 = input("What name?: ")

nome = " "
req = requests.post("https://teste1-18ed9-default-rtdb.firebaseio.com/.json", data=nome)
nome = req["5"][f"{value1}"]



print(req.json())