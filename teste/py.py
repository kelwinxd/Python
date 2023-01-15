




import pyautogui
import pyperclip
import time
import pandas

pyautogui.PAUSE = 1

# pyautogui.click -> clicar
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> conjunto de teclas
# pyautogui.write -> escreve um texto

# Passo 1: Entrar no sistema da empresa (no nosso caso é o link do drive)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=1025, y=489)
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
time.sleep(1.5)
pyautogui.press("enter")

time.sleep(4)

pyautogui.click(x=385, y=259, clicks=2)

time.sleep(2)

pyautogui.click(x=385, y=259)
pyautogui.click(x=1718, y=151)
pyautogui.click(x=1616, y=555)
time.sleep(2)

tabela = pandas.read_excel(r"C:\Users\Kelwin\Downloads\Vendas - Dez.xlsx")

print(tabela)






