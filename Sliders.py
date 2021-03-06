#Michael Pereira III




import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

from tkinter import *
from tkinter import Tk, Label, Button, StringVar
from tkinter import ttk
import tkinter as tk

import tkinter.filedialog
from tkinter import filedialog

from tkinter import Menu









import urllib
import json


#For images
import PIL
from PIL import ImageTk, Image

import pandas as pd
import numpy as np


LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize = (5,5), dpi = 100)
a = f.add_subplot(111)

def animate(i):
        pullData = open("sampleData.txt", "r").read()
        dataList = pullData.split('\n')
        xList = []
        yList = []
        for eachLine in dataList:
                if len(eachLine) > 1:
                        x, y = eachLine.split(',')
                        xList.append(int(x))
                        yList.append(int(y))
        a.clear()
        a.plot(xList, yList)

        



class ThreeDSynth(tk.Tk):
        def __init__(self, *args, **kwargs):
                tk.Tk.__init__(self, *args, **kwargs)

                tk.Tk.iconbitmap(self, "eighthnote.ico")
                tk.Tk.wm_title(self, "3D Synth")
                
                container = tk.Frame(self)
                container.pack(side = "top", fill = "both", expand = True)
                container.grid_rowconfigure(0, weight = 1)
                container.grid_columnconfigure(0, weight = 1)

                self.frames = {}

                for F in (StartPage, HomePage):

                        frame = F(container, self)

                        self.frames[F] = frame

                        frame.grid(row = 0, column = 0, sticky = "nsew")

                self.show_frame(StartPage)

        def show_frame(self, cont):
                frame = self.frames[cont]
                frame.tkraise()





class StartPage(tk.Frame):
        
        def __init__(self, parent, controller):
                #parent is name of parent class (ThreeDSynth)
                tk.Frame.__init__(self, parent)
                label = tk.Label(self, text = "Welcome to 3D Synth, an app that lets you create your own 3D song!", font = LARGE_FONT)
                label.pack(pady = 10, padx = 10)

                button1 = ttk.Button(self, text = "Get started", command = lambda:  controller.show_frame(HomePage))
                button1.pack()

                button2 = ttk.Button(self, text = "Exit", command = quit)
                button2.pack()

                homeImage = ImageTk.PhotoImage(Image.open("homepicture.jpg"))

                panel = tk.Label(self, image = homeImage)

                panel.pack(side = "bottom", fill = "both", expand = "yes")
                

        

                

     



class PageOne(tk.Frame):
        
        def __init__(self,parent, controller):
                tk.Frame.__init__(self,parent)
                label = tk.Label(self, text = "Start making your song. Hit the record button!", font = LARGE_FONT)
                label.pack(pady = 10, padx = 10)
                
                button1 = ttk.Button(self, text = "Return to Home", command = lambda:  controller.show_frame(StartPage))
                button1.pack()


               



                

class HomePage(tk.Frame):
        
        def __init__(self,parent, controller):
                tk.Frame.__init__(self,parent)
                label = tk.Label(self, text = "Welcome!", font = LARGE_FONT)
                label.pack(pady = 10, padx = 10)

                #For Home button
                button1 = ttk.Button(self, text = "Return to Home", command = lambda:  controller.show_frame(StartPage))
                button1.pack()

              
       


                

 

                canvas = FigureCanvasTkAgg(f, self)
                canvas.show()
                canvas.get_tk_widget().pack(side = tk.BOTTOM, fill = tk.BOTH, expand = True)


                toolbar = NavigationToolbar2TkAgg(canvas, self)
                toolbar.update()
                canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)

    

  
app = ThreeDSynth()
ani = animation.FuncAnimation(f, animate, interval = 1000)
app.mainloop()







                
                




##        def show_values():
##                print(w1.get(), w2.get())
##                master = Tk()
##                w1 = Scale(master, from_ = 0, to = 180, tickinterval = 30)
##                w1.pack()
##                w2 = Scale(master, from_=0, to=180, length=600,tickinterval=30, orient=HORIZONTAL)
##                w2.pack()
##                w3 = Scale(master, from_=0, to=180, length=600,tickinterval=30, orient=HORIZONTAL)
##                w3.pack()
##                w1.config(label = 'Y-axis')
##                w2.config(label = 'X-axis')
##                w3.config(label = 'Z-axis')


