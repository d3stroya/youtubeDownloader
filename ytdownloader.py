from pytube import YouTube
from tkinter import *

def descargar():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

root = Tk()
root.config(bd = 15)

root.title("YouTube Downloader\n")

descripcion = Label(root, text = "Añade el enlace del vídeo que quieres descargar y haz clic en el botón.\n")
descripcion.grid(row = 0, column = 0)

videos = Entry(root)
videos.grid(row = 2, column = 0)

boton = Button(root, text="Descargar", command = descargar)
boton.grid(row = 3, column = 0)

root.mainloop()