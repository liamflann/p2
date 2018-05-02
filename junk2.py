# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 15:26:47 2018

@author: liam
"""
import random
import sys
import csv
import os
import pandas as pd

def hangman():
    guessCount = 0
    def level():
        level = input("Which level do you want to play?", '\n',
                  "Easy, medium, or hard?")
        level= level.lower()
        
        if level == "easy":
            words = pd.read_csv("easy.txt", sep=" ",header=None)
        elif level == "medium":
            words = pd.read_csv("medium.txt", sep = " ", header=None)
        elif level == "hard":
            words = pd.read_csv("hard.txt", sep= " ", header = None)
        
        if level == "easy":
            f = open('easy.csv')
            csv_f = csv.reader(f)
            words = []
            for row in csv_f:
                words.append(row[0])
            secretWord = random.choice(words)
        elif level == "medium":
            f = open('medium.csv')
            csv_f = csv.reader(f)
            words = []
            for row in csv_f:
                words.append(row[0])
            secretWord = random.choice(words) 
        if level == "hard":
            f = open('hard.csv')
            csv_f = csv.reader(f)
            words = []
            for row in csv_f:
                words.append(row[0])
        secretword()
        return
    
    def secretword():
        secretWord = random.choice(words)
        guessed = "_" * len(secretWord)
        secretWord = list(secretWord)
        guessed = list(guessed)
        guess()
        return
    def guess():
        print("Here are the blanks for your secret word.")
        for char in secretWord:
            sys.stdout.write("_ ")
        guess = input("What is your guess? ")
        if (secretWord.find(guess) !=-1):
            correct()
        else:
            incorrect()
        return
    def incorrect():
        print("That letter is not present.")
        guessCount = guessCount + 1
        left = totalGuesses - guessCount
        print("You have {} guesses left.".format(left))
        return
    def correct():
        print("The letter is here.")
        loc = secretWord.find(guess)
        while (i < loc):
            sys.stdout.write("_ ")
            i=i+1
            if i == loc:
                break
        print(secretWord[loc], end=" ",flush=True)
        while (i < length-1):
            sys.stdout.write("_ ")
            i=i+1
        break

    
    level()
        
        
        

hangman()


#secretWord = "dog"
#length = len(secretWord)
#
#
#for char in secretWord:
#    sys.stdout.write("_ ")
#
#guess = input("What is your first guess? ")
#
#loc = secretWord.find(guess)
#
#
#guessCount = 0    
#
#while (guessCount < 10):
#    while (secretWord.find(guess) != -1):
#        print("Letter is there")
#        i = 0
#        while (i < loc):
#            sys.stdout.write("_ ")
#            i=i+1
#            if i == loc:
#                break
#        print(secretWord[loc], end=" ",flush=True)
#        while (i < length-1):
#            sys.stdout.write("_ ")
#            i=i+1
#        guess=(input("What is your next guess? "))
#        loc = secretWord.find(guess)
#    if(secretWord.find(guess) ==-1):
#        print("The letter is not here.")
#        guessCount = guessCount + 1
#        guess=(input("What is your next guess? "))
#        loc = secretWord.find(guess)
#    break
