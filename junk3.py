# -*- coding: utf-8 -*-
"""
Created on Wed May  2 12:38:06 2018

@author: liam
"""

import pandas as pd
import sys

secretWord = "mountainnnnn"
secretWord = secretWord.lower()
guessedWord = "_" * len(secretWord)
guessedWord = list(guessedWord)
word = list(secretWord)
usedLetters = []
counter = 0
def wrongGuess():
    global counter
    if counter < 5:
        counter = counter + 1
        left = 6 - counter
        print("You have {} guesses left".format(left))
        getGuess()
    elif counter == 5:
        print("You lose. Your the word was {}".format(secretWord))
        input("Want to play again? Y/N ")
   

def gotWord(guessedWord):
    gotIt = "_"*len(secretWord)
    if word == list(gotIt):
        input("You won! Press any key to exit")
    else:
        getGuess()
#Ask user for a letter
def getGuess():
    guess = input("What letter do you guess? ")
    checkforLetter(guess)
    return

def morethanoneLetter(secretWord, guess):
    print("The letter occurs more than once.")
    c = secretWord.count(guess) -1
    index = word.index(guess)
    guessedWord[index]=guess
    word[index]="_"
    print(' '.join(guessedWord))
    print("Please type the letter THEN press enter {} times".format(c))
    i = 0
    while i <= c:
        extra = input()
        index = word.index(extra)
        guessedWord[index]=extra
        word[index]="_"
        print(' '.join(guessedWord))
        i = i +1
        j = c - i
        if j > 0:
            print("Thanks, enter the letter {} more time(s)".format(j))
        if i == c:
            break
    gotWord(guessedWord)
    
def oneLetter(guess):
    index = word.index(guess)
    guessedWord[index]=guess
    word[index]="_"
    print(' '.join(guessedWord))
    gotWord(guessedWord)
    

def checkforLetter(guess):
    
    while (secretWord.find(guess)!=-1):
        print("The letter is there.")
        if (secretWord.count(guess) > 1):
            morethanoneLetter(secretWord,guess)
        else:
            oneLetter(guess)
    while (secretWord.find(guess) == -1):
        wrongGuess()
            
        
getGuess()
#if __name__ == '__main__':
#    wrongGuessCounter = 0
#    getGuess()