"""DudarKaitlynA2Q1
COMP 1012 SECTION A01
INSTRUCTOR Dr. Saulo Q. Dos Santos
ASSIGNMENT: A2 Question 1
AUTHOR Kaitlyn Dudar
VERSION [Date of last change; e.g., 2026-Feb-26]
PURPOSE: use of dictionaries to store and analyze word frequencies of two files
"""
def readWords(userWords):
    '''
    purpose: read the list of words the program will search for in the story
    return: list of words to count
    parameter: userWords is the filename containing the words
    '''
    fileWords= open(userWords, 'r')
    wordCount= fileWords.read().split() #split file into individual words
    fileWords.close()
    return wordCount

def readStory(userStory):
    """
    purpose: load the story so each word can be checked against the target list
    return: list of all words in the story
    parameter: userStory is the filename containing the story
    """

    fileStory= open(userStory, 'r')
    story=fileStory.read().split() #split story into individual words
    fileStory.close()
    return story

def countWords(wordCount, Story):
    """
    purpose: count how many times each target word appears in the story
    return: dictionary mapping each word to its count in the story
    parameters: wordList is list of target words, storyList is story words
    """

    counts= {} #THE DICTIONARY
    for word in wordCount: #every target word starts at 0
        counts[word]= 0
    for item in Story: #counting the occurrences by checking each story word
        if item in counts:
            counts[item]+= 1 #only counts words from the word list
    return counts

def uniqueWords(wordCount):
    """
    purpose: determine how many different words the program is tracking
    return: number of unique words being counted
    parameter: counts is the dictionary of word counts
    """

    numUniqueWords= len(wordCount)
    return numUniqueWords

def commonWords(counts):
    """
    purpose: identify which target word appears most often in the story
    return: the word with the highest frequency
    parameter: counts is the dictionary of word counts
    """

    words= list(counts.keys())
    mostword= words[0] #assumes the first word is the most common
    mostCount= counts[mostword]

    for word in words: #compares the word counts to find the highest
        if counts[word] > mostCount:
            mostword= word
            mostCount= counts[word]
    return mostword

def leastWords(counts):
    """
    purpose: identify which target word appears the least in the story
    return: the word with the lowest frequency
    parameter: counts is the dictionary of word counts
    """

    words= list(counts.keys())
    leastword= words[0] #assumes the first is the least common
    leastCount= counts[leastword]

    for word in words: #compares the word counts to find the minimum
        if counts[word] < leastCount:
            leastword= word
            leastCount= counts[word]
    return leastword

def alphabeticOrder(counts):
    """
    purpose: provide an alphabetical ordering for display
    return: list of words sorted alphabetically
    parameter: counts is the dictionary of word counts
    """

    alphabeticOrder= sorted(counts) #sorts dict keys alphabetically
    return alphabeticOrder

#Main Program
#user Inputs
userWords= input("Enter the name of the file containing the words to count: ")
userStory= input("Enter the name of the file containing the story: ")

#Reading the files
words= readWords(userWords)
story= readStory(userStory)

#count of the words
countedWords= countWords(words, story)

#Summary stores
numUnique = uniqueWords(countedWords)
mostCommon = commonWords(countedWords)
leastCommon = leastWords(countedWords)
alphaList = alphabeticOrder(countedWords)

#output
print("\nWords Counts: ")
for word in alphaList:
    print("The Word {} occurs {} times".format(word, countedWords[word]))
print("\nSummary:")
print("Total unique words searched: {}".format(numUnique))
print("Most common word: '{}' with {} occurrences".format(mostCommon, countedWords[mostCommon]))
print("Least common word: '{}' with {} occurrences".format(leastCommon, countedWords[leastCommon]))

print("\nAll words sorted alphabetically:")
for word in alphaList:
    print("'{}' occurs {} times.".format(word, countedWords[word]))

print("\nProgram terminated normally")
