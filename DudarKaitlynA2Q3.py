"""DudarKaitlynA2Q3
COMP 1012 SECTION A01
INSTRUCTOR Dr. Saulo Q. Dos Santos
ASSIGNMENT: A2 Question 3
AUTHOR Kaitlyn Dudar
VERSION [Date of last change; e.g., 2026-Feb-22]
PURPOSE: Analyze historical Bitcoin price data to calculate various statistics
"""
import math

def readFile(userInput):
    file= open(userInput)
    data= []
    for line in file:
        line= line.split() #have to come back to make it skip the header
        date, price= line.split(",")
        data.append(date, price)

    file.close()
    return data

def averagePrice(data):
    total= 0
    count= 0
    for date, price in data:
        total+= int(price)
        count+=1
    average= total/count
    return average, count

