import pyttsx3
from tkinter import *
oyna = Tk()
oyna.geometry('400x400')
oyna.title('Gapir')
def gapirish():
    pyttsx3.speak(kirit.get())
    return kirit
dasturchi = Label(text="Dasturchi: Obitov Suhrob", bg='red', font='Magneto')
dasturchi.place(x=90, y=240, width=240, height=40)
kirit = Entry()
kirit.place(x=105, y=70, width=200, height=50)
tugma = Button(text="Gapir", bg='lightblue', command=gapirish, font='Consolas')
tugma.place(x=90, y=160, width=230, height=40)
oyna.mainloop()
