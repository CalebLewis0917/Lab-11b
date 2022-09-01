# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab11b_Act1
# Date:         11 29 2021

import random

# Starts the game and initializes the random number
def startGame():
    num = random.randint(1,100)
    print("Guess the secret number! Hint: It's an integer between 1 and 100...")
    loop(num)

# Continues to ask the user to guess until they get it right    
def loop(num):
    guess = -1
    x = 0
    while(guess!=num):
        guess = int(input("What is your guess? "))
        if(guess<num):
            print("Too low!")
        elif(guess>num):
            print("Too high!")
        x += 1
    end(x)
  
# Ends the game and prints the results
def end(num):
    print("You guessed it! It took you " + str(num) + " guesses!")

# Hello? Comment
startGame()
# Hello? Comment