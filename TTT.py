
import random

from os import system, name  # define our clear function 

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
            
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('')



def playGame():
    result = 'Not Over'
    symbols = ('X', 'O')
    turn = 1
    playerTurn = (1,3,5,7,9) 
    computerTurn = (2,4,6,8)

    currentBoard = {'7': '7' , '8': '8' , '9': '9' ,
                    '4': '4' , '5': '5' , '6': '6' ,
                    '1': '1' , '2': '2' , '3': '3' }

    while result == 'Not Over' and turn < 10:
        clear()
        printBoard(currentBoard)
        #player1
        if turn in playerTurn:
            selection = 'wrong'
            selection = input("It is your turn. Where would you like to place an 'X'?")
            while selection not in currentBoard or currentBoard[selection] in symbols:
                clear()
                printBoard(currentBoard)
                selection = input("Incorrect selection. Where would you like to place an 'X'?")  
            currentBoard[selection] = 'X'  

        elif turn in computerTurn:
            #boardAtStartOfTurn = currentBoard
            totalPlayerMoves = sum(value == 'X' for value in currentBoard.values())   
            totalComputerMoves = sum(value == 'O' for value in currentBoard.values())

            if currentBoard['5'] not in symbols:
                currentBoard['5'] = 'O'
                totalComputerMoves = sum(value == 'O' for value in currentBoard.values())
            elif currentBoard['5'] == 'O':
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
            elif currentBoard['5'] == 'X':
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

             

            if totalPlayerMoves != totalComputerMoves:
                randomSelection = '5'
                while currentBoard[randomSelection] in symbols:
                    randomSelection = random.choice(list(currentBoard))
                currentBoard[randomSelection] = 'O'

            # if boardAtStartOfTurn == currentBoard:
            #     randomSelection = '5'
            #     while currentBoard[randomSelection] in symbols:
            #         randomSelection = random.choice(list(currentBoard))
            #     currentBoard[randomSelection] = 'O'
        if turn >= 5:
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
        turn +=1 

    clear()
    printBoard(currentBoard)

    if result == "Game Over!" and turn - 1 in playerTurn:
        print(f"{result} Congratulations, You Won!") 
    elif result == "Game Over!" and turn - 1 in computerTurn:
        print(f"{result} Unlucky, You Lost!") 
    else:
        print("Game Over! Game Tied!") 


newGame = "Y"

while newGame == "Y":
    playGame()
    newGame = "choose"
    while newGame not in ("Y", "N"):
        newGame = input("Do you want to play again? (Y/N)").upper()
    
