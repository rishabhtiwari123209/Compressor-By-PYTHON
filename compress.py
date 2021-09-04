from tkinter import *
from time import strftime
from PIL import ImageTk, Image
import time
from playsound import playsound
import os
import random
from timeit import default_timer as timer

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import webbrowser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import wikipedia
import PIL
from PIL import Image
from tkinter import filedialog

import random
root = Tk()
root.title("typing")
root.geometry("1000x650+40+30")

def compress():
        mainWindow = Toplevel (root)
        mainWindow.config(bg='dark gray')
        f1=Label(mainWindow,fg="navy blue",bg="light green" ,font="comicsansms 23 bold",borderwidth=3,relief=GROOVE,text="Give  new name which will save after compressor").pack()
        v = StringVar()
        v1 = IntVar()
        entryBox = Entry(mainWindow,fg="aqua" ,font="comicsansms 23 bold",borderwidth=3,relief=GROOVE, textvariable=v).pack()
        f2=Label(mainWindow,fg="navy blue",bg="light green" ,font="comicsansms 23 bold",borderwidth=3,relief=GROOVE,text="Enter the Width of image").pack()

        entryBox1 = Entry(mainWindow,fg="aqua" ,font="comicsansms 23 bold",borderwidth=3,relief=GROOVE, textvariable=v1).pack()
        def click():
            t12=str(v.get())
            t=int(v1.get())
            filename = filedialog.askopenfilename(
                        initialdir="C:\\",
                        title="Select a File",
                        filetypes=(("Text files",
                                    "*.jpg*"),
                                ("all files",
                                    "*.*")))
            # os.startfile(filename)            
            width=t
            
            img=Image.open(filename)#1
            wprecentage=(width/float(img.size[0]))
            size=int((float(img.size[1])*float(wprectage)))
            imgs=img.resize((wdth,hsize),PIL.Image.ANTIALIAS)#2
            filename1 = filedialog.askdirectory("\\")           
            
            img.save(filename1+"\\"+t12+".jpg")

        testButton = Button(mainWindow,fg="aqua",bg="black" ,font="comicsansms 23 bold",borderwidth=3,relief=GROOVE, text='click to compress', command=click, padx=10).pack()
        b511=Button(mainWindow,text=" QUIT",bg="black",fg="aqua" ,font="comicsansms 23 bold",borderwidth=3,relief=GROOVE , command=lambda: mainWindow.destroy()).pack()
        mainWindow.mainloop()

canvas = Canvas(root, width=500, height=500)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("C:\\Users\\rishabh tiwari\\Pictures\\pixel\\user3.jpg"))
canvas.pack(side='top', fill='both', expand='yes')
canvas.create_image(0, 0, anchor=NW, image=img)
###frame
framegreen = Frame(root, bg="#000023")

framegreen.place(x=0, y=600, height=100, width=250)
###label
title = Label(framegreen, text="press for setting and about to", font=("Impact", 15, "italic"), bg="white", fg="red").place(x=5, y=1)
#
f2 = Frame(root)
f2.place(x=200, y=400, height=60, width=380)

b1 = Button(f2, font=("adobe arbic", 20, "italic"), text="press to get typing option", bg="Aqua", command=compress)
b1.place(x=200, y=410, height=10, width=300)
b1.pack()
# frame and button of QUIT
f3 = Frame(root)
f3.place(x=690, y=400, height=60, width=80)
b2 = Button(f3, font=("Impact", 20, "italic"), text="EXIT", bg="Aqua", command=lambda: root.destroy())
b2.place(x=650, y=460)
b2.pack()

work = Label(root, text="TYPING MASTER BY HARSH ", font=("Impact", 25, "italic"), bg="white",
             fg="Aqua").place(x=400, y=70)



root.mainloop()
             