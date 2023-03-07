import PySimpleGUI as sg

layout = [
    [sg.Text('text')],
    [sg.Input()],
    [sg.Button('send')]
]


window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
window.close