# Rock,Paper,Scissors.py
# by Jonathan M. 
# Date: April 9, 2021

# Imports:
from random import randint
import random

print("Hello, welcome to my Rock,Paper,Scissors game!!! ")

hand = ["Rock", "Paper", "Scissors"]
play_Again = True
player_score = 0
computer_score = 0
computer_hand = hand[randint(0, 2)]


while play_Again == True:
    player_hand = input("Rock, Paper, Scissors?: ")
    if player_hand ==  computer_hand:
        print("It's a tie. No points awarded")
    elif player_hand == "Rock":
        if computer_hand == "Paper":
            print("You lose! " + computer_hand + " beats " + player_hand)
            computer_score += 1
        else:
            print("You win! " + player_hand + " beats "+ computer_hand)
            player_score += 1
    elif player_hand == "Paper":
        if computer_hand == "Scissors":
            print("You lose! " + computer_hand + " beats " + player_hand)
            computer_score += 1
        else:
            print("You win! " + player_hand + " beats " + computer_hand)
            player_score += 1
    elif player_hand == "Scissors":
        if computer_hand == "Rock":
            print("You lose! " + computer_hand + " beats " + player_hand)
            computer_score += 1
        else:
            print("You win! " + player_hand + " beats " + computer_hand)
            player_score += 1
    else:
        print("Not a valid input.")
    
    # Current Score:
    print("Current Score:")
    print(" Player:" , player_score , " Computer:" , computer_score)
    
    play_Again = input("Play Again? (y/n):")
    if play_Again == "y":
        play_Again = True
        computer_hand = hand[randint(0, 2)]
    else:
        play_Again = False
    print("-------------------------------------------")
    



