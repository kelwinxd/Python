import requests
import json
from email.mime.text import MIMEText
import time

from email.mime.text import MIMEText
import subprocess

# Define o conteúdo a ser escrito no arquivo
conteudo = "O preço abaixou"

# Define o caminho e o nome do arquivo
caminho_arquivo = "C:\\Users\\Kelwin\\Desktop\\Program\\file.txt"
#C:\Users\Kelwin\Desktop\Program
# Abre o Bloco de Notas e escreve o conteúdo no arquivo


url = 'https://www.udemy.com/api-2.0/courses/the-complete-javascript-course/'

header = {
  "Accept": "application/json, text/plain, */*",
  "Authorization": "Basic RnhZdUtGS094aDhFdzhZZmMwT0pKSXc2R1pWbVNhMkM4M1FWTnp5dTpzcGlkZXJtZW0zMjE=",
  "Content-Type": "application/json"
}






while True:

 response = requests.get(url, headers=header)



 price = response.json()['price']
 priceEdit = json.dumps(price).replace('R$','').strip()
 objPrice = json.loads(priceEdit)
 floatP = float(objPrice)

 if floatP < 180:
    subprocess.Popen(['notepad.exe', caminho_arquivo])
    with open(caminho_arquivo, 'w') as arquivo:
     arquivo.write(conteudo)


 print(floatP)
 time.sleep(5)
 
 


