"""DudarKaitlynA2Q2
COMP 1012 SECTION A01
INSTRUCTOR Dr. Saulo Q. Dos Santos
ASSIGNMENT: A2 Question 2
AUTHOR Kaitlyn Dudar
VERSION [Date of last change; e.g., 2026-Feb-26]
PURPOSE: calculates floor occupancy for flexible parking pricing
"""
'''
I choose to use a list with dictionaries, this keeps the three values together and
is a lot easier to use then index positions. By using it in a dictionary
I can just call the key.
'''
def rate(occupancy):
    """
    purpose: determine the correct parking rate for a given occupancy level
    return: parking rate based on occupancy percentage
    parameter: occupancy is the percent of spaces filled on a floor
    """
    if occupancy >= 75:
        RATE= 3
        return RATE
    elif occupancy >= 60 and occupancy < 75:
        RATE= 2
        return RATE
    elif occupancy >= 50 and occupancy < 60:
        RATE= 1.50
        return RATE
    else:
        RATE= 1
        return RATE

#main
userfile= input("Please enter the .csv file for the parkade: ")
file= open(userfile)

floorData= [] #This is the list that will store the dictionary for each floor.

for line in file:
    items = line.strip().split(",") #Splits the line into 3 values

    floorNum= int(items[0]) #Converts the floor number into a int the following do the same but for there given
    totSpace= int(items[1]) #Total Spaces
    vehicles= int(items[2]) #Total Vecicles

    data= {'Floor':floorNum, 'Spaces':totSpace, 'Vehicles':vehicles} #Stores the floor info in a dict
    floorData.append(data) #Adding the dict to the list

file.close()

#finds the spaces and all the vehicles across floors
space= 0
totVehicles= 0

for item in floorData:
    space= space + item['Spaces']
    totVehicles= totVehicles + item['Vehicles']

openSpace= space - totVehicles #Total open Spaces
occupancy= int((totVehicles / space) * 100) #total parkade occupancy

#outputs
if openSpace == 0: #Runs if the parkade it completely full
    print("PARKADE FULL")
else: #we look at each floor
    for item in floorData:
        floor= item['Floor'] #floor number
        spaces= item['Spaces'] #Total spaces on floor
        vehicles= item['Vehicles'] #Vechiles in parkade

        floorSpace= spaces - vehicles #open spaces on the floor
        floorOccupancy= int((vehicles/spaces)*100) #floor occupancy percentage

        if vehicles == spaces: #only runs if the floor is full
            print("Floor {}: FLOOR FULL".format(floor))
        else: #Calculates the rate based on the floors occupancy
            parkingRate= rate(floorOccupancy)
            print("Floor {}: {} spaces open, {}% occupancy, parking rate is ${:.2f}".format(floor, floorSpace, floorOccupancy, parkingRate))

#summary prints for both full and not full
print("----------\nTotal spaces in parkade: {}\nTotal available spaces: {}\nTotal parkade occupancy: {}%".format(space, openSpace, occupancy))

print("\nProgram terminated normally.")