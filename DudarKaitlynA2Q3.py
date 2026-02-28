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
        line= line.strip()

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

    return maxInc, maxIncDate

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

    return maxDec, maxDecDate

userInput= input("Enter the name of the bitcoin price file (.csv): ")

file = readFile(userInput)
avg, count = averagePrice(file)
minDate, minPrice = minPrice(file)
maxDate, maxPrice = maxPrice(file)
dev = deviation(file)
incCount = priceIncrease(file)
decCount = priceDecrease(file)
incAmount, incDate = dayIncrease(file)
decAmount, decDate = dayDecrease(file)

print("Bitcoin Price Statistics\n========================\n")
print("Price Statistics:")
print("Average Price: ${:,.2f}".format(avg))
print("Minimum Price: ${:,.2f} on {}".format(minPrice, minDate))
print("Maximum Price: ${:,.2f} on {}".format(maxPrice, maxDate))
print("Standard Deviation: ${:,.2f}".format(dev))

print("\nPrice Movement Analysis:")
print("Days with price increase: {}".format(incCount))
print("Days with price decrease: {}".format(decCount))
print("Largest single-day increase: ${:,.2f} on {}".format(float(incAmount), incDate))
print("Largest single-day decrease: ${:,.2f} on {}".format(float(decAmount), decDate))

print("Program terminated normally.")
