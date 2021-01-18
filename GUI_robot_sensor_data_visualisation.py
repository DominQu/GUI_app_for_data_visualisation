import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math
import numpy as np


FONT = ("Verdana", 12)
FONT2 = ("Arial", 12, "bold")
#add your file path
filepath = ""
num = 25
sens = 0


with open(filepath, "r") as file:
        data = file.readlines()
        datalen = len(data)
        numbers = []
        for line in data:
            singlel = line.split()
            singlel = [float(z) for z in singlel]
            numbers.append(singlel)
        sensorval = np.array(numbers)


class Compass:
    def __init__(self, canvas, parent, values, sens):
        self.canvas = canvas
        self.parent = parent
        self.values = values
        self.sensor = sens
        self.bounds = np.shape(self.values)
        self.labelN = ttk.Label(self.parent, text="North", font= FONT2)
        self.labelN.grid(row=1, column=1)

        self.labelW = ttk.Label(self.parent, text="West", font= FONT2)
        self.labelW.grid(row=2, column=0)

        self.labelE = ttk.Label(self.parent, text="East", font= FONT2)
        self.labelE.grid(row=2, column=2)

        self.labelS = ttk.Label(self.parent, text="South", font= FONT2)
        self.labelS.grid(row=3, column=1)

        self.canvas.create_oval(0,0,300,300,fill="black")
        self.canvas.create_line(150,150, 150, 0, arrow=tk.LAST,width=5, fill="red", tag="arrow")

        self.defaultangle = self.values[num][self.sensor]
        self.i = num
        self.angle = self.calAngle()
        self.STOPflag = False
        self.delay = 40

    def calAngle(self):
        return (self.values[self.i][self.sensor]- self.defaultangle)

    def changeFlag(self):
        self.STOPflag = not self.STOPflag

    def PauseandPlay(self):
        self.changeFlag()
        self.animateArrow()

    def setSens(self, sensor, label):
        self.sensor = sensor
        if sensor == 0:
            l = "Pitch"
        elif sensor == 1:
            l = "Roll"
        elif sensor == 2:
            l = "Yaw"
        label.configure(text=l)
        self.Reset(self.i)

    def draw(self):
        if self.STOPflag == True:
            self.changeFlag()
        self.animateArrow()

    def Reset(self, start):
        if self.STOPflag == False:
            self.changeFlag()
        if start > self.bounds[0] or start < 0:
            messagebox.showerror(title="Error", message="""Index out of bounds!
Enter a new one.""")
            self.changeFlag()
            return
        self.i = start
        self.defaultangle = self.values[start][self.sensor]
        self.angle = self.calAngle()

    def calDelay(self, freq):
        if freq <=0 or freq > 100:
            messagebox.showerror(title="Error", message="""This frequency is not supported!""")
            return
        ms = 1000/freq
        self.delay = int (round(ms))
        self.Reset(self.i)
        self.draw()

    def animateArrow(self ):
        if self.i == self.bounds[0]-1:
            self.STOPflag = False
            messagebox.showinfo(title="Info", message="No more data to visualize.")
            return    
        y = 300.0 - (math.sin(math.radians(self.angle) + math.pi/2)*150+150)
        x = math.cos(math.radians(self.angle) + math.pi/2)*150+150
        self.i +=1
        self.angle = self.calAngle()
        self.canvas.delete("arrow")
        self.canvas.create_line(150,150, x, y, arrow=tk.LAST,width=5, fill="red", tag="arrow")
        if not self.STOPflag:
            self.canvas.after(self.delay, self.animateArrow)

root = tk.Tk()
root.title("SensorViz")
label = ttk.Label(root, text="Pitch", font= FONT)
label.grid(row=0, column=0, columnspan=3)

label1 = ttk.Label(root, text="Liczba odrzuconych:", font=FONT)
label1.grid(row=0, column=3, columnspan=2)

label2 = ttk.Label(root, text="Częstotliwość odczytu:", font=FONT)
label2.grid(row=3, column=3, columnspan=2)

v1 = tk.StringVar()
n1 = tk.Entry(root, width=10, text=v1)
n1.grid(row=1, column = 4)
v1.set("25")      

v2 = tk.StringVar()
n2 = tk.Entry(root, width=10, text=v2)
n2.grid(row=4, column = 4)
v2.set("25")    

piccanvas = tk.Canvas(root,width = 300, height=300)
piccanvas.grid(row=2, column=1)
compass = Compass(piccanvas, root, sensorval, sens)

button1 = ttk.Button(root, text="Pause/Play",
command = lambda: compass.PauseandPlay())
button1.grid(row=2, column=4)

button2 = ttk.Button(root, text="Start",
command = lambda: compass.draw())
button2.grid(row=2, column=3)

button3 = ttk.Button(root, text="Reset",
command = lambda: compass.Reset(int(n1.get())))
button3.grid(row=1, column=3)

button4 = ttk.Button(root, text="Pitch",
command = lambda: compass.setSens(0, label))
button4.grid(row=4, column=0)

button5 = ttk.Button(root, text="Roll",
command = lambda: compass.setSens(1, label))
button5.grid(row=4, column=1)

button6 = ttk.Button(root, text="Yaw",
command = lambda: compass.setSens(2, label))
button6.grid(row=4, column=2)

button7 = ttk.Button(root, text="Change freq",
command = lambda: compass.calDelay(int(n2.get())))
button7.grid(row=4, column=3)

root.mainloop()
