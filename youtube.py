from pytube import YouTube
from PySimpleGUI import PySimpleGUI as sg 

sg.theme("reddit")
layout = [
    [sg.Text("URL"), sg.Input(key="url")],
    [sg.Button("Fazer o Download")]
],

janela = sg.Window("Video Downloader", layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
            break
    if eventos == "Fazer o Download":
        link = valores["url"] 
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        






