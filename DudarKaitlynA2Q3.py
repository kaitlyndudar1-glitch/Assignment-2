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
            data.append((date, float(price)))

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
    minDate, minPrice= data[0]
    for date, price in data:
        if price < minPrice:
            minDate, minPrice= date, price
    return minDate, minPrice

def maxPrice(data):
    maxDate, maxPrice= data[0]
    for date, price in data:
        if price > maxPrice:
            maxDate, maxPrice= date, price
    return maxDate, maxPrice

def deviation(data):
    average, count = averagePrice(data)
    total= 0

    for date, price in data:
        total+= (price - average)**2

    return math.sqrt(total/count)

def priceIncrease(data):
    countInc= 0

    for item in data:
        date, price= data[item-1]
        currentDate, currentPrice= data[item]
        difference= currentPrice - price
        if difference > 0:
            countInc+= 1
    return countInc

def priceDecrease(data):
    countDec= 0

    for item in range(1 , len(data)):
        date, price= data[item-1]
        currentDate, currentPrice= data[item]
        difference= currentPrice - price
        if difference < 0:
            countDec+= 1
    return countDec

def dayIncrease(data):
    for item in range(1 , len(data)):
        date, price= data[item-1]
        currentDate, currentPrice= data[item]
        difference= currentPrice - price

        if difference >

