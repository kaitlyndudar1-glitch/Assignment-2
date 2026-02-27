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
        line= line.split()