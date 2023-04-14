from tkinter import *
from tkinter import ttk, messagebox

screen = Tk()
#Title
screen.title("Current Conversor")

# Set the screen not resizable
screen.resizable(False, False)
screen.config(background="#3A3967",highlightcolor="black")

#define size of screen

largura = 500
altura = 500

# resulução do sistema
larguta_tela = screen.winfo_screenwidth()
altura_tela =  screen.winfo_screenmmheight()

# posicao da tela
posix = larguta_tela/2 - largura/2
posiy = altura_tela/2 - altura/2 + 300

# definir a geometry
screen.geometry("%dx%d+%d+%d" % (largura,altura,posix,posiy))





#every text begging with label
texting = Label(screen, text="", bg="#3A3967")
# Grid decides where it will place in column ow row
texting.place(x=100,y=200)


# its a input


nameImage = PhotoImage(file="Tkinter/ret1.png")
Boxsearch = Label(image=nameImage, bg="#3A3967")
Boxsearch.place(x=50, y=50)


name = Entry(screen, bg="#000000", border=0, fg="white", font=("poppins", 15, "bold"))
name.place(x=85, y=55)
name.focus()


#importing image

imgsearch = PhotoImage(file="Tkinter/search.png")
SearchButton = Button(screen, image=imgsearch, bg="black", border=0)
SearchButton.place(x=310, y=58)





screen.mainloop()