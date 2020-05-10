import numpy as np

filepath = "/home/dominik/Pulpit/data/outputPendulumOrt02.log"
#filepath = "C:/Users/Dominik/Desktop/outputPendulumOrt02.log"

#reading and processing data
with open(filepath, "r") as file:
    data = file.readlines()
numbers = []
for line in data:
    singlel = line.split()
    singlel = [float(z) for z in singlel]
    numbers.append(singlel)
sensorval = np.array(numbers)   