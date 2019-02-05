# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:12:37 2019

@author: Austin Seals
"""

import pandas as pd
import random as rd

# board game definition as dictionary
board = {"0": ['_', '_', '_'],
        "1": ['_','_','_'],
            "2":['_','_','_']}

# converting board to datframe
br_ = pd.DataFrame(data = board)


#function to receive player x coordinates
def player_x_input():
    player_x_input.row = input("Enter the row:")
    player_x_input.col = input ("Enter the column:")
    player_x_input.irow = int(player_x_input.row)
    player_x_input.icol = int(player_x_input.col)
    

# function to validate and make  move 
def validate_x():
    if br_.iloc[player_x_input.irow, player_x_input.icol] == '_':
        br_.iloc[player_x_input.irow, player_x_input.icol] = 'x'
    else:
        print("Invalid move!! Cell is already taken")
        
# function to check for winner 
# le is letter of player: x or o
# returns true is there is a winner
def isWinner(le):
    return  ((br_.iloc[0,0] == le and br_.iloc[0,1] == le and br_.iloc[0,2] == le) or # across the top
             (br_.iloc[1,0] == le and br_.iloc[1,1] == le and br_.iloc[1,2] == le) or # across the middle
             (br_.iloc[2,0] == le and br_.iloc[2,1] == le and br_.iloc[2,2] == le) or  # across the bottom
             (br_.iloc[0,0] == le and br_.iloc[1,0] == le and br_.iloc[2,0] == le) or # column 0
             (br_.iloc[0,1] == le and br_.iloc[1,1] == le and br_.iloc[2,1] == le) or # column 1 
             (br_.iloc[0,2] == le and br_.iloc[1,2] == le and br_.iloc[2,2] == le) or # column 2
             (br_.iloc[0,0] == le and br_.iloc[1,1] == le and br_.iloc[2,2] == le) or #diagonal
             (br_.iloc[2,0] == le and br_.iloc[1,1] == le and br_.iloc[0,2] == le))  # diagonal

def isFull():
  br_f =  br_ != '_'
  br_f.any()
   
    


# is the board full
gameIsPlaying = True
    
## This section of code is for AI portion of the game

def computer_move():
    center= br_.iloc[1,1]
    ########################################
    #function to make for the AI to make corner move
    def cornerMove():
       
       corners= [1,2,3,4 ]
       mv1 = rd.choice(corners)
       if mv1 == 1:
            if br_.iloc[0,0] == '_': 
                br_.iloc[0,0] = 'o'
            elif br_.iloc[0,0] == 'x':
                cornerMove()
       elif mv1 == 2:
           if br_.iloc[0,2] == '_': 
                br_.iloc[0,2] = 'o'
           elif br_.iloc[0,2] == 'x':
                cornerMove()
       elif mv1 == 3:
           if br_.iloc[2,0] == '_': 
                br_.iloc[2,0] = 'o'
           elif br_.iloc[2,0] == 'x':
                cornerMove()
       elif mv1 == 4:
           if br_.iloc[2,2] == '_': 
                br_.iloc[2,2] = 'o'
           elif br_.iloc[2,2] == 'x':
                cornerMove()
                
    # function to make a side move
    def sideMove():
        sides = [5,6,7,8]
        mv2 = rd.choice(sides)
        if mv2 == 5:
            if br_.iloc[1,0] == '_':
                br_.iloc[1,0] = 'o'
            elif br_.iloc[1,0] == 'x':
                sideMove()
        elif mv2 == 6:
            if br_.iloc[0,1] == '_':
                br_.iloc[0,1] = 'o'
            elif br_.iloc[0,1] == 'x':
                sideMove()
        elif mv2 == 7:
            if br_.iloc[1,2] == '_':
                br_.iloc[1,2] = 'o'
            elif br_.iloc[1,2] == 'x':
                sideMove()
        elif mv2 == 8:
            if br_.iloc[2,1] == '_':
                br_.iloc[2,1] = 'o'
            elif br_.iloc[2,1] == 'x':
                sideMove()
            
    ############################################
    if center == '_':
        br_.iloc[1,1] = 'o'
    
    elif center != '_':
        cornerMove()
    else:
        sideMove()
    
 
    
# testing 
print("WELCOME TO TIC TAC TOE!!")
print("You are player x and you have the first move!!")
print("Use coordinates to enter your move!!")   
print(br_)
while gameIsPlaying:
    player_x_input()
    validate_x()
    if isWinner('x'):
        print(br_)
        print("Congrats! You beat me AI")
        gameIsPlaying = False
    else:
        if isFull():
            print(br_)
            print("The game is a tie!")
            break
    # Computers turn 
    computer_move()
    if isWinner('o'):
        print(br_)
        print("You lose!!")
        gameIsPlaying = False 
    elif isFull():
        print(br_)
        print("The game is a tie!")
        break
        
    print(br_)

