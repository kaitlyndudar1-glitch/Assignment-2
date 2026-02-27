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


