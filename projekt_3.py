import numpy as np

filepath = "/home/dominik/Pulpit/data/outputPendulumOrt02.log"

#uploading and reading data
with open(filepath, "r") as file:
    data = file.readlines()
