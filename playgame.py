# -*- coding: utf-8 -*-
"""

This is a collection of games. There is a dice game, and a number guessing game

Algorithm:
    Ask user which game they want to play
    Select function with that game
    Ask the user if they want to play that game again
    Ask the user if they want to choose a different game instead
Hope to add Hangman to it later.
@author: liam
"""

#Collection of games project.

import numpy as np
import random
import pandas as pd
import csv
import sys

#Ask the user which game s/he wants to play. Call that function.
def gamechoice():
    print("Which game would you like to play? Dice, Guess, Hangman")
    game = input()    
    game = game.lower()
    if game == 'dice':
        dice()
    elif game == 'guess':
        guess()  
    elif game == 'hangman':
        hangman()
    return

#Exit screen
def thanksforplaying():
    print("Thanks for playing!")
    return

#Ask the user if s/he wants to play guess again
def playagain():
    print("Want to play again? Y/N")
    answer = input()
    answer = answer.lower()
    while (answer == 'y'):
        guess()
    if answer=='n':
        differentgame()
    return

#Ask the user if s/he wants to play dice again
def playagain2():
    print("Want to play again? Y/N")
    answer = input()
    answer = answer.lower()
    while (answer == 'y'):
        dice()
    if answer=='n':
        differentgame()
    return

#Ask the user if s/he wants to play a differen game. Call that function.
def differentgame():
    print("Would you like to play a different game?")
    answer = input()
    answer = answer.lower()
    if answer == 'y':
        gamechoice()
    else:
        thanksforplaying()
    return 0
    

def hangman():

    level = input("Which level do you want to play? Easy, medium, or hard? ")
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
    elif level == "hard":
        f = open('hard.csv')
        csv_f = csv.reader(f)
        words = []
        for row in csv_f:
            words.append(row[0])
        secretWord = random.choice(words) 
    elif level not in ["easy", "medium", "hard"]:
        print("I'm sorry, that's not a valid choice.")
        hangman()
        
    for char in secretWord:
        sys.stdout.write("_ ")

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
            print("You lose. The word was {}".format(secretWord))
            counter = 0
            answer = input("Want to play again? Y/N ")
            answer = answer.lower()
            while(answer == 'y'):
                hangman()
            if answer == 'n':
                differentgame()
    
    def gotWord(guessedWord):
        gotIt = "_"*len(secretWord)
        if word == list(gotIt):
            print("You won!")
            print("Want to play again? Y/N")
            answer = input()
            answer = answer.lower()
            while (answer == 'y'):
                hangman()
            if answer=='n':
                differentgame()
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
        if (secretWord.find(guess)!=-1):
            print("The letter is there.")
            if (secretWord.count(guess) > 1):
                morethanoneLetter(secretWord,guess)
            else:
                oneLetter(guess)
        else:
            print("Sorry, the letter is not there.")
            wrongGuess()
            
    getGuess()


    
        

    #thanksforplaying()
    return


"""This game rolls a die with a user specified number of sides. The program
counts the user's rolls, and the number of wins, losses, and ties. When the
user chooses not to play again, the program outputs the number of games played,
wins, losses, and ties. It goes to function to ask the user if s/he wants to
play a different game.
"""
def dice():
    
    #initialize the counters.
    win = 0
    loss = 0
    tie = 0
    
    #get user input, store this for the sides to determine random numbers
    print('How many sides does your die have? ')
    sides = int(input())
    
    print("Here's your firt roll: ")
    oldx = random.randint(1,sides)
    print(oldx)
    
    roll = input('Would you like to roll again? Y/N ')
    roll = roll.upper()
    #continue to roll as long as user wants to, add to the counters.
    while (roll=='Y'):
        x = random.randint(1,sides)
        print(x)
        newx = x
        if newx > oldx:
            print('You beat your last roll!')
            win = win + 1
        elif newx == oldx:
            print('You tied with your last roll.')
            tie = tie + 1
        else:
            print('You did not beat your last roll :(')
            loss = loss +1
        oldx = newx
        roll = input('Would you like to roll again? Y/N ')
        roll = roll.upper()
        
    
    total = win + loss + tie
    print('You played {} games and won {}, tied {}, and lost {}.'.format(
        total, win, loss, tie))
    playagain2()
    return

"""This game asks the user to guess a randomly generated number between
two randomly generated limits. The user is given a limit number of tries to
correctly guess the number. If s/he does, then the game terminates,
congradulates the user, and asks if s/he wants to play again. If s/he does
not guess the correct number in the number of tries, the program tells the 
user the correct answer, and asks if s/he wants to play again. If the user
does not want to play, the program directs to the choose another game function.
"""
def guess():
    limit1 = random.randint(-1000,1000)
    limit2 = random.randint(-1000,1000)
    #Control in place in case the limits are equal
    while(limit1==limit2):
        limit1 = random.randint(-1000,1000)
        limit2 = random.randint(-1000,1000)
        if limit1 != limit2:
            break
    #Determining upper and lower limits
    if limit1 > limit2:
        magicNum = random.randint(limit2, limit1)
        low = limit2
        high = limit1
    elif limit2 > limit1:
        magicNum = random.randint(limit1, limit2)
        low = limit1
        high = limit2
    print('Pick a number between {} and {}.'.format(low,high))
    userNum = int(input())
    if userNum == magicNum:
        print("Good guess, you're right!")
    guessCount = 0
    while (guessCount <10):
        while (userNum != magicNum):
            if userNum < magicNum:
                print("Sorry, too low.")
            elif userNum > magicNum:
                print("Sorry, too high.")
            userNum = int(input())
            if userNum == magicNum:
                print("You're right! It took {} guesses.".format(guessCount))
                playagain()
                break
            guessCount = guessCount + 1
            if guessCount >= 10:
                print("Sorry, you took too many guess. Game over.")
                print("The magic number was {}.".format(magicNum))
                playagain()
                break
        break
    return

#The main function of this program.
if __name__ == '__main__':
   gamechoice()
   input("Press ENTER to exit")
   

