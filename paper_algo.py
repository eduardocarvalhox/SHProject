import pandas as pd

#Open file
filename = "example1.txt"
txt = open(filename)

#Read the number of cities
txt.readline()
txt.readline()
line = txt.readline()
ncities = int(line.split()[1])

#Read the table of cities' positions
cities_positions = pd.read_csv('example1.txt', sep='\t', header = None, skiprows = 10, nrows = ncities)
cities_positions.columns = ["City", "X", "Y"]

