#Sorry I didn't have time to write the report

import random #to all us to generate a random move

from os import system, name  #to allow us to clear the terminal

def clear(): #define the clear function
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
            
def printBoard(board): #to allow us to print out the board
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('')



def playGame(): #define the game
    result = 'Not Over' #to allow us to keep playing until we have a winner
    symbols = ('X', 'O') #acceptable symbols on the board
    turn = 1 #turn number
    playerTurn = (1,3,5,7,9) #turns in which the player must move
    computerTurn = (2,4,6,8) #turns in which the computer must move

    currentBoard = {'7': '7' , '8': '8' , '9': '9' , #to maintain the current state of the board
                    '4': '4' , '5': '5' , '6': '6' ,
                    '1': '1' , '2': '2' , '3': '3' }

    while result == 'Not Over' and turn < 10: #loop through each move until the game is over
        clear() #clear the terminal
        printBoard(currentBoard) #print the board 
        #player1
        if turn in playerTurn: #loop through if it is the player's turn
            selection = 'wrong' #set default for player input
            selection = input("It is your turn. Where would you like to place an 'X'?") #ask for player input
            while selection not in currentBoard or currentBoard[selection] in symbols: #loop through until input is acceptable
                clear()
                printBoard(currentBoard)
                selection = input("Incorrect selection. Where would you like to place an 'X'?")  
            currentBoard[selection] = 'X'  #update the current state of the board

        elif turn in computerTurn: #loop through if it is the computer's turn
           
            totalPlayerMoves = sum(value == 'X' for value in currentBoard.values()) #count number of turns taken by player
            totalComputerMoves = sum(value == 'O' for value in currentBoard.values()) #count number of turns taken by computer

            if currentBoard['5'] not in symbols: #if the middle square has not been taken, always take it first
                currentBoard['5'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
            #check if the computer can win on this turn
            elif currentBoard['5'] == 'O': #if the middle square is an 'O', we first check to see if the computer can win on the diagonals or the cross in the centre
                if currentBoard['7'] and currentBoard['3'] != 'X': 
                    if currentBoard['7'] == 'O':
                        currentBoard['3'] = 'O'
                    elif currentBoard['3'] == 'O':
                        currentBoard['7'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                if (currentBoard['1'] and currentBoard['9'] != 'X') and (totalPlayerMoves != totalComputerMoves): 
                    if currentBoard['1'] == 'O':
                        currentBoard['9'] = 'O'
                    elif currentBoard['9'] == 'O':
                        currentBoard['1'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                if (currentBoard['4'] and currentBoard['6'] != 'X') and (totalPlayerMoves != totalComputerMoves): 
                    if currentBoard['4'] == 'O':
                        currentBoard['6'] = 'O'
                    elif currentBoard['6'] == 'O':
                        currentBoard['4'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                if (currentBoard['8'] and currentBoard['2'] != 'X') and (totalPlayerMoves != totalComputerMoves): 
                    if currentBoard['8'] == 'O':
                        currentBoard['2'] = 'O'
                    elif currentBoard['2'] == 'O':
                        currentBoard['8'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
            elif currentBoard['5'] == 'X': #if the middle square is an 'X', we only need to check if the computer can win on the top & bottom rows and the flanks
                if currentBoard['7'] and currentBoard['8'] and currentBoard['9'] != 'X': 
                    if currentBoard['7'] and currentBoard['8'] == 'O':
                        currentBoard['9'] = 'O'
                    elif currentBoard['7'] and currentBoard['9'] == 'O':
                        currentBoard['8'] = 'O'
                    elif currentBoard['8'] and currentBoard['9'] == 'O':
                        currentBoard['7'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                if (currentBoard['7'] and currentBoard['4'] and currentBoard['1'] != 'X') and (totalPlayerMoves != totalComputerMoves): 
                    if currentBoard['7'] and currentBoard['4'] == 'O':
                        currentBoard['1'] = 'O'
                    elif currentBoard['7'] and currentBoard['1'] == 'O':
                        currentBoard['4'] = 'O'
                    elif currentBoard['1'] and currentBoard['4'] == 'O':
                        currentBoard['7'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                if (currentBoard['1'] and currentBoard['2'] and currentBoard['3'] != 'X') and (totalPlayerMoves != totalComputerMoves): 
                    if currentBoard['1'] and currentBoard['2'] == 'O':
                        currentBoard['3'] = 'O'
                    elif currentBoard['1'] and currentBoard['3'] == 'O':
                        currentBoard['2'] = 'O'
                    elif currentBoard['2'] and currentBoard['3'] == 'O':
                        currentBoard['1'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                if (currentBoard['9'] and currentBoard['6'] and currentBoard['3'] != 'X') and (totalPlayerMoves != totalComputerMoves): 
                    if currentBoard['9'] and currentBoard['6'] == 'O':
                        currentBoard['3'] = 'O'
                    elif currentBoard['9'] and currentBoard['3'] == 'O':
                        currentBoard['6'] = 'O'
                    elif currentBoard['3'] and currentBoard['6'] == 'O':
                        currentBoard['9'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())

            #check if the computer needs to block the player from winning on the next turn
            if currentBoard['5'] == 'X' and (totalPlayerMoves != totalComputerMoves): #if the middle square is an 'X', we first check if we need to block the diagonals and the cross in the centre
                if currentBoard['7'] == 'X' and currentBoard['3'] in symbols:
                        currentBoard['3'] = 'O'
                        totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                elif currentBoard['3'] == 'X' and currentBoard['7'] in symbols:
                        currentBoard['7'] = 'O'
                        totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                elif currentBoard['1'] == 'X' and currentBoard['9'] in symbols:
                        currentBoard['9'] = 'O'
                        totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                elif currentBoard['9'] == 'X' and currentBoard['1'] in symbols:
                        currentBoard['1'] = 'O'
                        totalComputerMoves = sum(value == 'O' for value in currentBoard.values())


            if currentBoard['5'] == 'O': #if the middle square is an 'O', we heck if we must block the top and bottom rows and the flanks
                if currentBoard['7'] and currentBoard['8'] and currentBoard['9'] != 'O': 
                    if currentBoard['7'] and currentBoard['8'] == 'X':
                        currentBoard['9'] = 'O'
                    elif currentBoard['7'] and currentBoard['9'] == 'X':
                        currentBoard['8'] = 'O'
                    elif currentBoard['8'] and currentBoard['9'] == 'X':
                        currentBoard['7'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                if (currentBoard['7'] and currentBoard['4'] and currentBoard['1'] != 'O') and (totalPlayerMoves != totalComputerMoves): 
                    if currentBoard['7'] and currentBoard['4'] == 'X':
                        currentBoard['1'] = 'O'
                    elif currentBoard['7'] and currentBoard['1'] == 'X':
                        currentBoard['4'] = 'O'
                    elif currentBoard['1'] and currentBoard['4'] == 'X':
                        currentBoard['7'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                if (currentBoard['1'] and currentBoard['2'] and currentBoard['3'] != 'O') and (totalPlayerMoves != totalComputerMoves): 
                    if currentBoard['1'] and currentBoard['2'] == 'X':
                        currentBoard['3'] = 'O'
                    elif currentBoard['1'] and currentBoard['3'] == 'X':
                        currentBoard['2'] = 'O'
                    elif currentBoard['2'] and currentBoard['3'] == 'X':
                        currentBoard['1'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
                if (currentBoard['9'] and currentBoard['6'] and currentBoard['3'] != 'O') and (totalPlayerMoves != totalComputerMoves): 
                    if currentBoard['9'] and currentBoard['6'] == 'X':
                        currentBoard['3'] = 'O'
                    elif currentBoard['9'] and currentBoard['3'] == 'X':
                        currentBoard['6'] = 'O'
                    elif currentBoard['3'] and currentBoard['6'] == 'X':
                        currentBoard['9'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
      
            if totalPlayerMoves != totalComputerMoves: #if the computer cant win and doesnt need to block, make a random move
                randomSelection = '5'
                while currentBoard[randomSelection] in symbols:
                    randomSelection = random.choice(list(currentBoard))
                currentBoard[randomSelection] = 'O'

            
        if turn >= 5: #from turn 5, check if there is a winner
            if currentBoard['7'] == currentBoard['8'] == currentBoard['9']: 
                result = "Game Over!"
            elif currentBoard['4'] == currentBoard['5'] == currentBoard['6']:
                result = "Game Over!"
            elif currentBoard['1'] == currentBoard['2'] == currentBoard['3']:
                result = "Game Over!"
            elif currentBoard['7'] == currentBoard['4'] == currentBoard['1']:        
                result = "Game Over!"
            elif currentBoard['8'] == currentBoard['5'] == currentBoard['2']:
                result = "Game Over!"
            elif currentBoard['9'] == currentBoard['6'] == currentBoard['3']:
                result = "Game Over!"
            elif currentBoard['7'] == currentBoard['5'] == currentBoard['3']:
                result = "Game Over!"
            elif currentBoard['9'] == currentBoard['5'] == currentBoard['1']:
                result = "Game Over!"
        turn +=1 #move to next turn

    clear()
    printBoard(currentBoard)

    #print the winner
    if result == "Game Over!" and turn - 1 in playerTurn:
        print(f"{result} Congratulations, You Won!") 
    elif result == "Game Over!" and turn - 1 in computerTurn:
        print(f"{result} Unlucky, You Lost!") 
    else:
        print("Game Over! Game Tied!") 


newGame = "Y" #set default to yes

while newGame == "Y": #run the game
    playGame() #play the game. This always runs at least once
    newGame = "choose" #reset default
    while newGame not in ("Y", "N"): #ask user if they want to play again, until they enter an acceptable value
        newGame = input("Do you want to play again? (Y/N)").upper()
    
