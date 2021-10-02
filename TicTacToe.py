#Tic-Tac-Toe Game :
#Basic_TicTacToe_game_by_Pragya:

board = {'top-L' :' ','top-M':' ','top-R':' ',
         'mid-L' :' ','mid-M':' ','mid-R':' ',
         'low-L' :' ','low-M':' ','low-R':' '}


def printBoard():
    print("             "+board['top-L'] + '        |           ' + board['top-M'] + '          |           ' + board['top-R'])
    print('     ______________________________________________________________')
    print("             "+board['mid-L'] + '        |           ' + board['mid-M'] + '          |           ' + board['mid-R'])
    print('     ______________________________________________________________')
    print("             "+board['low-L'] + '        |           ' + board['low-M'] + '          |           ' + board['low-R'])
turn = 'X'



def condition_to_win():

    if board['top-L'] == board['top-M'] and board['top-M'] == board['top-R'] and board['top-M'] != " ":
        
        print("\nplayer with turn {} is the winner !!\n\n".format(board['top-L']))
        flag =0
    elif board['mid-L'] == board['mid-M'] and board['mid-M'] == board['mid-R'] and board['mid-M'] != " ":
        
        print("\nplayer with turn {} is the winner!!\n\n".format(board['mid-L']))
        flag =0
    elif board['low-L']== board['low-M'] and board['low-M'] == board['low-R']and board['low-M'] != " ":
        
        print("\nplayer with turn {} is the winner !!\n\n".format(board['low-L']))
        flag =0
    elif board['top-L'] == board['mid-L'] and board['mid-L'] == board['low-L']and board['top-L'] != " ":
        
        print("\nplayer with turn {} is the winner !!\n\n".format(board['top-L']))
        flag =0
    elif board['top-M'] == board['mid-M'] and board['mid-M'] == board['low-M']and board['top-M'] != " ":
        
        print("\nplayer with turn {} is the winner !!\n\n".format(board['top-M']))
        flag =0
    elif board['top-R'] == board['mid-R'] and board['mid-R'] == board['low-R']and board['top-R'] != " ":
        
        print("\nplayer with turn {} is the winner !!\n\n".format(board['top-R']))
        flag = 0
    elif board['top-L'] == board['mid-M'] and board['mid-M'] == board['low-R']and board['top-L'] != " ":
        
        print("\nplayer with turn {} is the winner !!\n\n".format(board['top-L']))
        flag = 0
    elif board['top-R'] == board['mid-M'] and board['mid-M'] == board['low-L']and board['top-R'] != " ":
        
        print("\nplayer with turn {} is the winner !!\n\n".format(board['top-R']))
        flag =0
    else:
        flag = 1

    return flag

print("\n\n                 Welcome to Simple Tic-Tac-Toe Game !!\n\n")
print("\n                                               Rules:\n")
print("                                 Use: --> top-L, top-M, top-R")
print("                                          mid-L, mid-M, mid-R ")
print("                                          low-L, low-M, low-R\n\n")
flag = 1
for i in range(1,10):
    printBoard()
    print("\n\n")
    print('     Turn for ' + turn + '. Move on which space?')
    move = input()
    board[move] = turn
    
    if i >= 4:
        f = condition_to_win()
        if f == 0:
            printBoard()
            print("\n\n")
            break
        if f == 1 and i == 9:
            print("\n\n         Draw!!      :(\n\n")
            printBoard()
            print("\n\n")
            break
        
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
    
















































