# You will be supplied with two data files in CSV format. The first file contains
# statistics about various dinosaurs. The second file contains additional data.
#
# Given the following formula,
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)
#
# Write a program to read in the data files from disk, it must then print the names
# of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.

# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.2,herbivore
# Struthiomimus,0.92,omnivore
# Velociraptor,1.0,carnivore
# Triceratops,0.87,herbivore
# Euoplocephalus,1.6,herbivore
# Stegosaurus,1.40,herbivore
# Tyrannosaurus Rex,2.5,carnivore


# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.87,quadrupedal
# Stegosaurus,1.90,quadrupedal
# Tyrannosaurus Rex,5.76,bipedal
# Hadrosaurus,1.4,bipedal
# Deinonychus,1.21,bipedal
# Struthiomimus,1.34,bipedal
# Velociraptor,2.72,bipedal


import csv
import math
dino_strideLength = {}
dino_leglenth = {}
dino_speed = {}

file_path1 = "c:/Users/shara/OneDrive/Desktop/Dinosaur_Problem/dataset1.csv"
file_path2 = "c:/Users/shara/OneDrive/Desktop/Dinosaur_Problem/dataset2.csv"

with open(file_path2, 'r') as csv_file:
    readCSV = csv.reader(csv_file, delimiter = ',')
    for rows in readCSV:
        if rows[2] == "bipedal":
            dino_strideLength.update({rows[0]:rows[1]})
    print(dino_strideLength)

with open(file_path1,'r') as csv_file:
    readCSV = csv.reader(csv_file,delimiter = ',')
    for rows in readCSV:
        if rows[0] in dino_strideLength:
            dino_leglenth.update({rows[0]:rows[1]})
    print(dino_leglenth)

for i in dino_leglenth:
    if i in dino_strideLength:
        speed = ((float(dino_strideLength[i])/float(dino_leglenth[i])) - 1) * math.sqrt(float(dino_leglenth[i]) * 9.8)
        dino_speed.update({i:speed})

print(dino_speed)
dino_speed = reversed(sorted(dino_speed.items(), key = lambda x : x[1]))
for i in dino_speed:
    print(i[0])