"""DudarKaitlynA2Q1
COMP 1012 SECTION A01
INSTRUCTOR Dr. Saulo Q. Dos Santos
ASSIGNMENT: A2 Question 1
AUTHOR Kaitlyn Dudar
VERSION [Date of last change; e.g., 2026-Feb-26]
PURPOSE: use of dictionaries to store and analyze word frequencies of two files
"""
from distributed.diagnostics.progress_stream import counts


def readWords(userWords):
    fileWords= open(userWords)
    wordCount= fileWords.read().split()
    fileWords.close()
    return wordCount

def readStory(userStory):
    fileStory= open(userStory)
    story=fileStory.read().split()
    fileStory.close()
    return story

def countWords(wordCount, Story):
    counts= {}
    for word in wordCount
    counts[word]= 0
    for item in Story:
        if item == word:
            counts[word]+= 1
    return counts

def uniqueWords(wordCount)
    numUniqueWords= len(wordCount)
    return numUniqueWords

def commonWords():
    mostCommon= max(counts)

def leastWords()
    LeastWords= min(counts)

def