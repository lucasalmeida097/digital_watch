from tkinter import *
from datetime import datetime
import pyglet
pyglet.font.add_file("digital-7.ttf")

###### Colors used #######
color1 = "#3d3d3d"  # preta
color2 = "#fafcff"  # branca
color3 = "#21c25c"  # verde
color4 = "#eb463b"  # vermelha
color5 = "#dedcdc"  # cinza
color6 = "#3080f0"  # azul

background = color1
color = color3

window = Tk()
window.title("")
window.geometry('440x180')
window.resizable(width = FALSE, height = FALSE)
window.configure(bg=background)


def clock():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    dayWeek = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")

    l1.config(text=hour)
    l1.after(200, clock)
    l2.config(text=dayWeek + " " + str(day) + "/" + str(month) + "/" + str(year)) 


l1 = Label(window, text="", font="digital-7 100", bg=background, fg=color)
l1.grid(row=0, column=0, stick=NW, padx=5)
l2 = Label(window, text="", font="digital-7 17", bg=background, fg=color)
l2.grid(row=1, column=0, stick=NW, padx=5)


clock()
window.mainloop()