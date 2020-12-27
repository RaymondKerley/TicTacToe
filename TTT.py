theBoard = {'7': '7' , '8': '8' , '9': '9' ,
            '4': '4' , '5': '5' , '6': '6' ,
            '1': '1' , '2': '2' , '3': '3' }
            
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


theBoard['7'] = '7'
 

for turn in range(10):
    printBoard(theBoard)
    selection = 'wrong'
    selection = input("It is your turn. Where would you like to place an X?")
    while selection not in theBoard: #('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        selection = input("Incorrect selection. Where would you like to place an X?")
        printBoard(theBoard)
        
'''
         if theBoard[selection] != 'X' or 'Y':
        # theBoard[selection] = 'X'
        # else:
        #     selection = ''
'''