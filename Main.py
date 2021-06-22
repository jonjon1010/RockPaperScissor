'''
Created on Jun 22, 2021
Program: Rock, Paper, Scissor Game 
@author: Jonathan Nguyen
'''
import random 
import math 

play = "yes" 
while play.lower() == "yes":
    print("This is a game of rock, paper, and scissor")
    rounds = input("How many rounds would you like to play: ")
    while rounds.isdigit() == False:
        print("The input enter was not a number.")
        rounds = input("Please enter how many rounds would you like to play again: ")
    userWins = 0
    compWins = 0
    while userWins < math.ceil(int(rounds)/2) and compWins < math.ceil(int(rounds)/2):
        print("----------------------------------------------------------------------------------------------")
        userChoice = input("Enter your choose of either rock, paper, or scissor: ")
        print("Your choose", userChoice.lower())
        while userChoice.lower() != "rock" and userChoice.lower() != "paper" and userChoice.lower != "scissor":
            print("\nYou have entered a wrong input.")
            userChoice = input("Please enter your choose of either rock, paper, or scissor again: ")
            print("You choose", userChoice.lower())
        ListChoice =["rock","paper","scissor"]; 
        compChoose = random.choice(ListChoice)
        print("The computer choose",compChoose)
        while userChoice == compChoose:
            print("\nIt's a draw, please enter your choose of either rock, paper, or scissor again: ")
            print("You choose", userChoice.lower())
            compChoose = random.choice(ListChoice)
            print("The computer choose",compChoose)
        if userChoice.lower() == "rock" and compChoose == "paper":
            print("paper bets rock, the winner is the computer.")
            compWins += 1
        elif userChoice.lower() == "paper" and compChoose == "rock":
            print("paper bets rock, the winner is the user.")
            userWins += 1
        elif userChoice.lower() == "paper" and compChoose == "scissor":
            print("scissor bets paper, the winner is the computer.")
            compWins += 1
        elif userChoice.lower() == "scissor" and compChoose == "paper":
            print("scissor bets paper, the winner is the user.")
            userWins += 1
        elif userChoice.lower() == "scissor" and compChoose == "rock":
            print("rock bets scissor, the winner is the computer.")
            compWins +- 1
        elif userChoice.lower() == "rock" and compChoose == "scissor":
            print("rocks bets scissor, the winner is the user.")
            userWins += 1
        print("The number of wins between the user and computer is:", "user -",userWins, ": computer -",compWins)
        print("----------------------------------------------------------------------------------------------")
    if userWins > compWins:
        print("The winner of the game is the user!!!")
    else:
        print("The winner of the game is the computer!!")
    play = input("Do you want to play again? choose either yes or no:")
    while play.lower() != "yes" and play.lower() != "no":
        play = input("You entered and invalid input.Do you want to play again? choose either yes or no: ")
print("----------------------------------------------------------------------------------------------")
print("Thank you for playing!!!")
        
    
        