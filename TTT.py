theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
            
def printBoard(board):
    print(board['7'] + ' | ' + board['8'] + '| ' + board['9'])
    print('--|--|--')
    print(board['4'] + ' | ' + board['5'] + '| ' + board['6'])
    print('--|--|--')
    print(board['1'] + ' | ' + board['2'] + '| ' + board['3'])


theBoard['7'] = 'X'
printBoard(theBoard) 

# Decide who goes first


acceptableSelections = ("h", "head", "heads", "t", "tail", "tails") #Define acceptable user inputs

decideFirstMove = "" #Request the user to input Heads or Tails
while decideFirstMove not in acceptableSelections:
    decideFirstMove = input("Lets decide who goes first. Choose Heads(H) or Tails(T):").lower()

if decideFirstMove in ("h", "head", "heads"): 
    coinSelection = 0 #Assign Heads to 0
else:
    coinSelection = 1 #Assign Tails to 1

import random
coinToss = random.randint(0,1) #Random coin toss
if coinToss == 0:
    print("The coin landed on Heads")
else:
    print("The coin landed on Tails")

if coinSelection == coinToss: #Compare user selection to the result of the coin toss
    print("Congratulation! You go first")
else:
    print("Unlucky! You will go second")
