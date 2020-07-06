#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:18:04 2020

@author: amnagul
"""

# Opening & reading a text file in python
#song = open('Song_lyrics.txt', 'r')
#print(song.read())



# creating a list of words 
with open('Song_lyrics.txt') as f:
    wordList = f.read().split()

print('Here are the lyrics for a song: \n', wordList, '\n')

def lyricsToFreq(myList):
    """
        dicionary of each word's frequency
    """
    wordFreqDict = {}
    for word in wordList:
        if word in wordFreqDict:
            wordFreqDict[word] += 1
        else:
            wordFreqDict[word] = 1
        
    return wordFreqDict
    

def mostCommonWords(myDict):
    """
        words that occured max number of times
    """
    freq = myDict.values()
    best = max(freq)
    
    words = []
    for i in myDict:
        if myDict[i] == best:
            words.append(i)
            
    return (words, best)

def wordsOccurMinTimes(myDict, minTimes):
    """
        all words occuring atleast minTimes in song
    """
    result = []
    done = False
    
    copyDict = myDict.copy()
    while not done:
        temp = mostCommonWords(copyDict)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(copyDict[w])
        else:
            done= True
        
    return result
    
    


mydict = lyricsToFreq(wordList)
print('Frequency of each word in the song:\n', mydict, '\n')

(w, b) = mostCommonWords(mydict)
print('Most common words in this song are: \n', (w, b), '\n')

result = wordsOccurMinTimes(mydict, 10)
print('All words occuring atleast 10 times in this song are: \n', (w, b), '\n')
print(result)