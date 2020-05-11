import numpy as np
import tkinter as tk 
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import turtle
import math


FONT = ("Verdana", 12)
num = 25

filepath = "/home/dominik/Pulpit/data/outputPendulumOrt02.log"
#filepath = "C:/Users/Dominik/Desktop/outputPendulumOrt02.log"

#reading and processing data
class dataREAD:
    def __init__(self, filepath):
        with open(filepath, "r") as file:
            data = file.readlines()
        numbers = []
        for line in data:
            singlel = line.split()
            singlel = [float(z) for z in singlel]
            numbers.append(singlel)
        sensorval = np.array(numbers)

#window creating class
class APProot(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "SensorViz")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for FR in (FrontPage, PitchValPage, RollValPage, YawValPage):
            frame = FR(container, self)
            self.frames[FR] = frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(FrontPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
#launching page        
class FrontPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Podaj liczbę n-pierwszych wartości do odrzucenia", font= FONT)
        label.pack(pady=10,padx=10)

        
        n = tk.Entry(self, width=10)
        n.pack()
        
        def submit(ent):
            num = int(ent)
            print(num)
            
        button1 = ttk.Button(self, text="Submit",
        command = lambda: submit(n.get()))
        button1.pack()

        label1 = ttk.Label(self, text="Teraz przejdź do wartości, którą chcesz zobaczyć", font= FONT)
        label1.pack(pady=10,padx=10)

        button2 = ttk.Button(self, text="Pitch Value Page",
        command = lambda: controller.show_frame(PitchValPage))
        button2.pack()

        button3 = ttk.Button(self, text="Roll Value Page",
        command = lambda: controller.show_frame(RollValPage))
        button3.pack()

        button4 = ttk.Button(self, text="Yaw Value Page",
        command = lambda: controller.show_frame(YawValPage))
        button4.pack()
#Pitch values page
class PitchValPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Pitch", font= FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Front",
        command = lambda: controller.show_frame(FrontPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6], [4,5,3,7,6,8])

        pltcanvas = FigureCanvasTkAgg(f, self)
        pltcanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(pltcanvas, self)
        toolbar.update()
        pltcanvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        piccanvas = tk.Canvas(self,width = 300, height=300)
        piccanvas.pack(side=tk.TOP)

        Compass(piccanvas)
     

#Roll values page
class RollValPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Pitch", font= FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Front",
        command = lambda: controller.show_frame(FrontPage))
        button1.pack()
#Yaw values page
class YawValPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Pitch", font= FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Front",
        command = lambda: controller.show_frame(FrontPage))
        button1.pack()
#drawing the compass
class Compass(turtle.RawTurtle):
    def __init__(self, canvas):
        turtle.RawTurtle.__init__(self, canvas)
        self.screen.bgcolor('black')
        self.pensize(5)
        self.shape("classic")
        self.color('red')
        self.up()
        #draw N
        self.setpos(-5,125)
        self.setheading(90.0)
        self.down()
        self.forward(20)
        self.goto(5,125)
        self.forward(20)
        self.up()
        #draw E
        self.setposition(145,10)
        self.setheading(180.0)
        self.down()
        self.forward(10)
        self.left(90.0)
        self.forward(10)
        self.left(90.0)
        self.forward(10)
        self.up()
        self.goto(135,0)
        self.right(90.0)
        self.down()
        self.forward(10)
        self.left(90.0)
        self.forward(10)
        self.up()
        #draw S
        self.setposition(5,-130)
        self.left(90.0)
        self.down()
        self.circle(5,180)
        self.goto(5,-140)
        self.circle(-5,180)
        self.up()
        #draw W
        self.setposition(-145,10)
        self.down()
        self.goto(-140,-10)
        self.goto(-135,10)
        self.goto(-130,-10)
        self.goto(-125,10)
        self.up()
        self.home()
        self.color("green")
        self.setheading(90.0)
    def pointer(startingangle, newangle):
        angle = newangle-startingangle
        Compass.setheading(angle)
        Compass.down()
        Compass.forward(100)
        Compass.update()

app = APProot()
Compass.pointer(14.0,78.0)
app.mainloop()