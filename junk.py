# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:08:58 2018

@author: liam
"""

import pandas as pd
import random
import sys
def thanksforplaying():
    print("Thanks for playing!")
    return

 
secretWord = "mountain"
length = len(secretWord)


for char in secretWord:
    sys.stdout.write("_ ")

guess = input("What is your first guess? ")

loc = secretWord.find(guess)
guessedWord = "_" * len(secretWord)
guessedWord = list(guessedWord)

word = list(secretWord)
usedLetters = []

guessCount = 0 

def gameover():
    print("Thanks for playing.")

def guess():
    guessCount = 0 
    while (guessCount < 20):
        guess = input("What is your guess: ")
        guessCount = guessCount + 1
        isletterthere(guess)
        if (guessCount ==20):
            gameover()
            break
    return guess

def isletterthere(guess):
    numberofLetters = secretWord.count(guess)
    if (secretWord.find(guess) !=-1):
        if(numberofLetters>1):
            morethanoneletter()
        else:
            printletters()
    else:
        print("Sorry, the letter is not there.")
    return

def printletters():
    index = word.index(guess)
    guessedWord[index]=guess
    word[index]="_"
    print(''.join(guessedWord))
    guess()
    return

def morethanoneletter():
    letterCount = 0
    while (letterCount <= numberofLetters):
        index = word.index(guess)
        guessedWord[index]=guess
        word[index]="_"
        print(''.join(guessedWord))
        if letterCount == numberofLetters:
            guess()
            break
    return
    
guess()
#while (guessCount < 10):
#    while (secretWord.find(guess) != -1):
#
#        print("Letter is there")
#        if (numberofLetters > 1):
#            morethanoneletter()
#        else:
#            index = word.index(guess)
#            guessedWord[index]=guess
#            word[index]="_"
#            print(''.join(guessedWord))
#        
#
#        
#        i = 0
##        while (i < loc):
##            sys.stdout.write("_ ")
##            i=i+1
##            if i == loc:
##                break
##        print(secretWord[loc], end=" ",flush=True)
##        usedLetters.insert(loc, guess)
##        for guess in usedLetters:
##            print(guess, end = "_",flush=True)
##        while (i < length-1):
##            sys.stdout.write("_ ")
##            i=i+1
##        print(usedLetters, end = " ")
#        guess=(input("What is your next guess? "))
#        loc = secretWord.find(guess)
#    if(secretWord.find(guess) ==-1):
#        print("The letter is not here.")
#        guessCount = guessCount + 1
#        guess=(input("What is your next guess? "))
#        loc = secretWord.find(guess)
#    break
