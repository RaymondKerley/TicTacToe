currentBoard = {'7': '7' , '8': '8' , '9': '9' ,
                '4': '4' , '5': '5' , '6': '6' ,
                '1': '1' , '2': '2' , '3': '3' }

symbols = ('X', 'O')
playerTurn = (1,3,5,7,9) 
computerTurn = (2,4,6,8)
turn = 1

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


for move in range(10):
    clear()
#player1
    if turn in playerTurn:
        printBoard(currentBoard)
        selection = 'wrong'
        
        selection = input("It is your turn. Where would you like to place an X?")
        while selection not in currentBoard or currentBoard[selection] in symbols:
            clear()
            printBoard(currentBoard)
            selection = input("Incorrect selection. Where would you like to place an X?")  
        currentBoard[selection] = 'X'   
        turn +=1 
    #printBoard(currentBoard)

#player2
    clear()
    if turn in computerTurn:
        printBoard(currentBoard)
        selection = 'wrong'
        clear()
        printBoard(currentBoard)
        selection = input("It is your turn. Where would you like to place an O?")
        while selection not in currentBoard or currentBoard[selection] in symbols:
            clear()
            printBoard(currentBoard)
            selection = input("Incorrect selection. Where would you like to place an O?")  
        currentBoard[selection] = 'O'   
        turn +=1 
   