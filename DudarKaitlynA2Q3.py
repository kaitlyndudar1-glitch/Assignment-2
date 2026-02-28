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
    devi= math.sqrt(total/count)
    return devi

def priceIncrease(data):
    countInc= 0

    for item in range(1 , len(data)):
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
    date, price= data[0]
    currentDate, currentPrice= data[1]

    difference= currentPrice - price
    maxInc= difference
    maxIncDate= currentDate

    for item in range(1 , len(data)):
        date, price= data[item-1]
        currentDate, currentPrice= data[item]

        difference= currentPrice - price

        if difference > maxInc:
            maxInc= difference
            maxIncDate= currentDate

    return maxIncDate, maxInc

def dayDecrease(data):
    date, price= data[0]
    currentDate, currentPrice= data[1]

    difference= currentPrice - price
    maxDec= difference
    maxDecDate= currentDate

    for item in range(1 , len(data)):
        date, price= data[item-1]
        currentDate, currentPrice= data[item]

        difference= currentPrice - price

        if difference < maxDec:
            maxDec= difference
            maxDecDate= currentDate

    return maxDecDate, maxDec

userInput= input("Enter the name of the bitcoin price file (.csv): ")

file = readFile(userInput)
avg, count = averagePrice(file)
minDate, minPrice = minPrice(file)
maxDate, maxPrice = maxPrice(file)
dev = deviation(file)
incCount = priceIncrease(file)
decCount = priceDecrease(file)
incDate, incAmount = dayIncrease(file)
decDate, decAmount = dayDecrease(file)


