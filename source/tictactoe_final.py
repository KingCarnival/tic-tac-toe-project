# -*- coding: utf-8 -*-
"""
AI Tic Tac Toe
Maching Intelligence Assignment   
Created on Fri Feb  1 11:12:37 2019

@authors: Austin Seals, Shubahm Patel and Preston Bruce
"""

# importing the packages we need. PANDAS for data manipulation and RANDOM for 
# AI decsion making 
import pandas as pd
import random as rd

#  tic tac toe board  definition as dictionary
board = {"0": ['_', '_', '_'],
        "1": ['_','_','_'],
            "2":['_','_','_']}

# converting board to datframe
br_ = pd.DataFrame(data = board)


#function to receive player move coordinates
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

def isFull(): # is the game a tie? if so return true
  if (br_.iloc[0,0] != '_' and br_.iloc[0,1] != '_' and br_.iloc[0,2] != '_' and
      br_.iloc[1,0] != '_' and br_.iloc[1,1] != '_' and br_.iloc[1,2] != '_' and
      br_.iloc[2,0] != '_' and br_.iloc[2,1] != '_' and br_.iloc[2,2] != '_' ):
      return True 
  else:
        pass

# This variable controls the flow the game
# As long as this variable is true the game continues   
gameIsPlaying = True
    

## This section of code is for AI portion of the game###################

def computer_move():
    center= br_.iloc[1,1]
    ########################################
    #function to make for the AI to make corner move
    def cornerMove():
       
       corners= [1,2,3,4 ] # each number is associated with a different corner
       mv1 = rd.choice(corners)
       if mv1 == 1:
            if br_.iloc[0,0] == '_': 
                br_.iloc[0,0] = 'o'
                return True
            elif br_.iloc[0,0] == 'x':
                cornerMove()
       elif mv1 == 2:
           if br_.iloc[0,2] == '_': 
                br_.iloc[0,2] = 'o'
                return True
           elif br_.iloc[0,2] == 'x':
                cornerMove()
       elif mv1 == 3:
           if br_.iloc[2,0] == '_': 
                br_.iloc[2,0] = 'o'
                return True
           elif br_.iloc[2,0] == 'x':
                cornerMove()
       elif mv1 == 4:
           if br_.iloc[2,2] == '_': 
                br_.iloc[2,2] = 'o'
                return True
           elif br_.iloc[2,2] == 'x':
                cornerMove()
       else:
            pass
    # function to make a side move
    def sideMove():
       sides = [5,6,7,8] # each number is associated with a different side
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
    
      
        
    def rowBlockOp(): # iterate throgh each row and determine if the user has a winning move then block
        rows=[0,1,2]
        
        for row in rows:
            list1 = list()
            list2 = list()
            list1 = br_.iloc[row].values.tolist()
            if list1.count('x') == 2:
                if '_' in list1:
                    list2 = br_.iloc[row].replace(to_replace = '_', value = 'o')
                    br_.iloc[row] = list2
                    return True
                    break
     
    
    def colBlockOp(): # iterate throgh each column and determine if the user has a winning movethen block
        
        cols = ['0','1','2']
        for col in cols:
            list1 = list()
            list2 = list()
            list1 = br_[col].tolist()
            if list1.count('x') == 2:
                if '_' in list1:
                    list2 = br_[col].replace(to_replace = '_', value = 'o')
                    br_[col] = list2
                    return True
                    break
    
    def diagBlock(): # test and see if the user can win diagonally and block
        if br_.iloc[0,0] == 'x' and br_.iloc[1,1] == 'x':
            if br_.iloc[2,2] == '_':
                br_.iloc[2,2] = 'o'
                return True
        elif br_.iloc[2,0] == 'x' and br_.iloc[1,1] == 'x':
            if br_.iloc[0,2] == '_':
                br_.iloc[0,2] = 'o'
                return True
        elif br_.iloc[2,2] == 'x' and br_.iloc[1,1] == 'x':
            if br_.iloc[0,0] == '_':
                br_.iloc[0,0] = 'o'
                return True
        elif br_.iloc[0,2] == 'x' and br_.iloc[1,1] == 'x':
            if br_.iloc[2,0] == '_':
                br_.iloc[2,0] = 'o'
                return True
        else:
            pass
    
    def diagWin(): # test and see if the computer can win diagonally 
        if br_.iloc[0,0] == 'o' and br_.iloc[1,1] == 'o':
            if br_.iloc[2,2] == '_':
                br_.iloc[2,2] = 'o'
                return True
        elif br_.iloc[2,0] == 'o' and br_.iloc[1,1] == 'o':
            if br_.iloc[0,2] == '_':
                br_.iloc[0,2] = 'o'
                return True
        elif br_.iloc[2,2] == 'o' and br_.iloc[1,1] == 'o':
            if br_.iloc[0,0] == '_':
                br_.iloc[0,0] = 'o'
                return True
        elif br_.iloc[0,2] == 'o' and br_.iloc[1,1] == 'o':
            if br_.iloc[2,0] == '_':
                br_.iloc[2,0] = 'o'
                return True
        else:
            pass
    
    
    def winRow(): # the computer determines if it can win on the next  move by row  
        rows=[0,1,2]
        
        for row in rows:
            list1 = list()
            list2 = list()
            list1 = br_.iloc[row].values.tolist()
            if list1.count('o') == 2:
                if '_' in list1:
                    list2 = br_.iloc[row].replace(to_replace = '_', value = 'o')
                    br_.iloc[row] = list2
                    return True
                    break
                
    def winCol(): # the computer determines if it can win by column 
        
        cols = ['0','1','2']
        for col in cols:
            list1 = list()
            list2 = list()
            list1 = br_[col].tolist()
            if list1.count('o') == 2:
                if '_' in list1:
                    list2 = br_[col].replace(to_replace = '_', value = 'o')
                    br_[col] = list2
                    return True
                    break

    ############################################
    # AI decision algorthm
    if winRow() is True:
        pass
    elif diagWin() is True:
        pass
    elif winCol() is True:
        pass
    elif diagBlock() is True:
        pass
    elif rowBlockOp() is True:
        pass
    elif colBlockOp() is True:
        pass
    elif center == '_':
        br_.iloc[1,1] = 'o'
    
    elif cornerMove() is True:
        pass
    elif cornerMove() is True:
        sideMove()
    else:
        pass
    
#************************************************************
    
# Game implemetation 


print("WELCOME TO TIC TAC TOE!!")
print("You are player x and you have the first move!!")
print("Use coordinates to enter your move!!")   
print(br_)
while gameIsPlaying :
        player_x_input()
        validate_x()
        if isWinner('x'):
            print("Congrats! You beat me AI")
            gameIsPlaying = False
        elif isFull() is True:
                print("The game is a tie!")
                gameIsPlaying = False
        # Computers turn 
        computer_move()
        if isWinner('o'):
            print("You lose!!")
            gameIsPlaying = False 
        elif isFull() is True:
            print("The game is a tie!")
            gameIsPlaying = False
        print('')
        print(br_)  


 

