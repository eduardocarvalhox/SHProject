import pandas as pd

#Open file
filename = "example1.txt"
txt = open(filename)

#Read the number of cities
txt.readline()
txt.readline()
line = txt.readline()
ncities = line.split()[1]


