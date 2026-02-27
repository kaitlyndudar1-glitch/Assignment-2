"""DudarKaitlynA2Q2
COMP 1012 SECTION A01
INSTRUCTOR Dr. Saulo Q. Dos Santos
ASSIGNMENT: A2 Question 2
AUTHOR Kaitlyn Dudar
VERSION [Date of last change; e.g., 2026-Feb-26]
PURPOSE: calculates floor occupancy for flexible parking pricing
"""

def rate(occupancy):
    if occupancy >= 75:
        rate= 3
        return rate
    elif occupancy >= 60 and occupancy < 75:
        rate= 2
        return rate
    elif occupancy >= 50 and occupancy < 60:
        rate= 1.50
        return rate
    else:
        rate= 1
        return rate

userfile= input("Please enter the .csv file for the parkade: ")
file= open(userfile)

floorData= []

for line in file:
    items = line.strip().split(",")

    floorNum= int(items[0])
    totSpace= int(items[1])
    vehicles= int(items[2])

    data= {'Floor':floorNum, 'Spaces':totSpace, 'Vehicles':vehicles}
    floorData.append(data)

file.close()

space= 0
totVehicles= 0

for item in floorData:
    space= space + item['Spaces']
    totVehicles= totVehicles + item['Vehicles']

openSpace= space - totVehicles
occupancy= int((openSpace / space) * 100)

if openSpace == 0:
    print("PARKADE FULL\n----------\nTotal spaces in parkade: {}\nTotal available spaces: 0\nTotal parkade occupancy: 100%".format(space))

