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
    firstLine= "Date,Price"
    for line in file:
        line= line.split()

        if line != firstLine:
        date, price= line.split(",")
        data.append(date, float(price))

    file.close()
    return data

def averagePrice(data):
    total= 0
    count= 0
    for date, price in data:
        total+= price
        count+=1
    average= total/count
    return average, count

def minPrice(data):
    mindate, minprice= min(data)
    return mindate, minprice

def maxPrice(data):
    maxdate, maxprice= max(data)
    return maxdate, maxprice

def deviation(data):
    average, count = averagePrice(data)
    total= 0

    for date, price in data:
        total+= (price - average)**2

    return total/count


