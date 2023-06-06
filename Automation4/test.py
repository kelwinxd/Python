import pyautogui 
import time
import pandas
import pyperclip as pc
import subprocess



# Pressionar o AltGr + P
pyautogui.keyDown('alt')
pyautogui.keyDown('gr')
pyautogui.press('p')

# Realizar ação associada à hotkey AltGr + P

# Soltar o AltGr + P
pyautogui.keyUp('p')
pyautogui.keyUp('gr')
pyautogui.keyUp('alt')


