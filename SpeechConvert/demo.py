from gtts import gTTS
import os
from tkinter import *
from tkinter import filedialog

def textSpeech():
    text = entry.get()
    language = language_var.get()  # Obtém o idioma selecionado no menu suspenso
    output = gTTS(text=text, lang=language, slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')

def download_audio():
    text = entry.get()
    language = language_var.get()  # Obtém o idioma selecionado no menu suspenso
    output = gTTS(text=text, lang=language, slow=False)
    save_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if save_path:
        output.save(save_path)

root = Tk()
root.configure(bg='black')

canvas = Canvas(root, width=500, height=400, bg='black')
canvas.pack()

label = Label(root, text="Text to Speech", bg="black",fg="white", font=("Arial",30))
canvas.create_window(250,50,window=label)

fonte_entry = ("Arial", 19)

entry = Entry(root, font=fonte_entry)
canvas.create_window(250, 100, window=entry, width=250, height=28)

# Lista de opções para o idioma
idiomas = ["en", "es", "fr", "pt"]  # Adicione mais idiomas conforme necessário

# Variável para armazenar o idioma selecionado
language_var = StringVar(root)
language_var.set(idiomas[0])  # Define o primeiro idioma como o idioma padrão

# Criação do menu suspenso para selecionar o idioma
idioma_menu = OptionMenu(root, language_var, *idiomas)
canvas.create_window(250, 150, window=idioma_menu, width=100)

button_start = Button(text="Start", command=textSpeech)
canvas.create_window(165, 250, window=button_start, width=80)

button_download = Button(text="Download", command=download_audio)
canvas.create_window(335, 250, window=button_download, width=80)

root.mainloop()
