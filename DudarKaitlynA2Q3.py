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
    '''
    Purpose: Read file containing Bitcoin prices and convert each line into (date, price) tuple
    Return: A list of (date, price) tuples, where price is stored as a float
    Parameter: userInput — the filename of the CSV file to read
    '''
    file= open(userInput)
    data= [] #list that stores (date, price) tuple
    firstLine= "Date,Price" #the header of the file

    for line in file:
        line= line.strip()

        if line != firstLine: #skips the header line
            date, price= line.split(",") #split into date and price
            data.append((date, float(price))) #adds the date and the float price

    file.close()
    return data #list of tuples

def averagePrice(data):
    '''
    Purpose: finds the average Bitcoin price and counts how many exist
    Return: A tuple (averagePrice, count)
    Parameter: data — list of (date, price) tuples
    '''
    total= 0
    count= 0
    for date, price in data:
        total+= price #sums the prices
        count+=1
    average= total/count
    return average, count

def minPrice(data):
    '''
    Purpose: Find the minimum Bitcoin price and when date it was
    Return: A tuple (minDate, minPrice)
    Parameter: data — list of (date, price) tuples
    '''
    minDate, minPrice= data[0] #becomes the first entry
    for date, price in data:
        if price < minPrice: #checks if new min was found
            minDate, minPrice= date, price
    return minDate, minPrice

def maxPrice(data):
    '''
    Purpose: Find the maximum Bitcoin price and when date it was
    Return: A tuple (maxDate, maxPrice)
    Parameter: data — list of (date, price) tuples
    '''
    maxDate, maxPrice= data[0] #becomes the first entry
    for date, price in data:
        if price > maxPrice: #checks if new max was found
            maxDate, maxPrice= date, price
    return maxDate, maxPrice

def deviation(data):
    '''
    Purpose: Compute the standard deviation of all Bitcoin prices
    Return: The standard deviation as a float
    Parameter: data — list of (date, price) tuples
    '''
    average, count = averagePrice(data) #gets the average and count
    total= 0

    for date, price in data:
        total+= (price - average)**2 #squared diff of mean

    devi= math.sqrt(total/count) #standard deviation
    return devi

def priceIncrease(data):
    '''
    Purpose: Count how many days the Bitcoin price increased from the previous day
    Return: The number of days with increase
    Parameter: data — list of (date, price) tuples
    '''
    countInc= 0

    for item in range(1 , len(data)):
        date, price= data[item-1] #previous day
        currentDate, currentPrice= data[item] #current day
        difference= currentPrice - price
        if difference > 0: #check if price increased
            countInc+= 1
    return countInc

def priceDecrease(data):
    '''
    Purpose: Count how many days the Bitcoin price decreased from the previous day
    Return: The number of days with decrease
    Parameter: data — list of (date, price) tuples
    '''
    countDec= 0

    for item in range(1 , len(data)):
        date, price= data[item-1] #previous day
        currentDate, currentPrice= data[item] #current day
        difference= currentPrice - price
        if difference < 0: #check if price decreased
            countDec+= 1
    return countDec

def dayIncrease(data):
    '''
    Purpose: Find the largest single day price increase when it occurred
    Return: A tuple (maxIncrease, increaseDate)
    Parameter: data — list of (date, price) tuples
    '''
    date, price= data[0] #First day
    currentDate, currentPrice= data[1] #second day

    difference= currentPrice - price
    maxInc= difference
    maxIncDate= currentDate

    for item in range(1 , len(data)):
        date, price= data[item-1]
        currentDate, currentPrice= data[item]

        difference= currentPrice - price #diff

        if difference > maxInc: #checks if new max increase
            maxInc= difference
            maxIncDate= currentDate

    return maxInc, maxIncDate

def dayDecrease(data):
    '''
    Purpose: Find the largest single-day price decrease and when it occurred
    Return: A tuple (maxDecrease, decreaseDate)
    Parameter: data — list of (date, price) tuples
    '''
    date, price= data[0] #First day
    currentDate, currentPrice= data[1] #second day

    difference= currentPrice - price
    maxDec= difference
    maxDecDate= currentDate

    for item in range(1 , len(data)):
        date, price= data[item-1]
        currentDate, currentPrice= data[item]

        difference= currentPrice - price #diff

        if difference < maxDec: #checks if new max decrease
            maxDec= difference
            maxDecDate= currentDate

    return maxDec, maxDecDate

#main
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

#output
print("\nBitcoin Price Statistics\n========================\n")
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

print("\nProgram terminated normally.")
