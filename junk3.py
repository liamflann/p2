# -*- coding: utf-8 -*-
"""
Created on Wed May  2 12:38:06 2018

@author: liam
"""

import pandas as pd
import sys

secretWord = "mountain"
secretWord = secretWord.lower()
guessedWord = "_" * len(secretWord)
guessedWord = list(guessedWord)
word = list(secretWord)
usedLetters = []
counter = 0
def wrongGuess(counter):
    counter = counter + 1
    print(counter)
    getGuess()

#Ask user for a letter
def getGuess():
    guess = input("What letter do you guess? ")
    checkforLetter(guess, counter)
    return

def morethanoneLetter(secretWord, guess):

    print("nothing")
    getGuess()
    
def oneLetter(guess):
    index = word.index(guess)
    guessedWord[index]=guess
    word[index]="_"
    print(' '.join(guessedWord))
    getGuess()
    

def checkforLetter(guess, counter):
    if (secretWord.find(guess)!=-1):
        print("The letter is there.")
        if (secretWord.count(guess) > 1):
            morethanoneLetter(secretWord,guess)
        else:
            oneLetter(guess)
    else:
        print("Sorry, the letter is not there.")
        getGuess()
        

if __name__ == '__main__':
    wrongGuessCounter = 0
    getGuess()