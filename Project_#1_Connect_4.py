import numpy as np
column_count=7
row_count=6

def create_board():
    board=np.zeros((row_count,column_count))
    return board
def is_empty(board,col):
    if board[5][col]==0:
            return True  #checks if column has space

def next_row(board, column):
    for r  in range(row_count):
        if board[r][column]==0:
            return r  #checks the next empty row

def drop(row,col,board,piece):
    board[row][col]=piece

def final(board, piece):
    #checking horizontal         works
    for r in range(row_count):
        for c in range(column_count-3):
            if board[r][c]==piece and board[r][c]==board[r][c+1] and board[r][c+1]==board[r][c+2] and board[r][c+2]==board[r][c+3]:
                return True
    #checking vertical           works
    for r in range(row_count-3):
        for c in range(column_count):
            if board[r][c]==piece and board[r][c]==board[r+1][c] and board[r+1][c]==board[r+2][c] and board[r+2][c]==board[r+3][c]:
                return True
    #checking positive diagonal  /
    for r in range(5,row_count-3):
        for c in range(column_count - 3):
            if board[r][c]==piece and board[r][c] == board[r-1][c + 1] and board[r-1][c+1] == board[r-2][c+2] and board[r-2][c + 2] == board[r-3][
                c + 3]:
                return True
    #for negative diagonals       \ works
    for r in range(row_count-3):
        for c in range(column_count - 3):
            if board[r][c]==piece and board[r][c] == board[r+1][c + 1] and board[r+1][c + 1] == board[r+2][c + 2] and board[r+2][c + 2] == board[r+3][
                c + 3]:
                return True

game_over=True
turn=1
board=create_board()
print(board)

def print_board(board):
    print(np.flip(board,0))
while game_over:
    if turn==1:
        col=int(input("Enter the column no.(1) to put your piece: "))
        if is_empty(board,col):
            row=next_row(board,col)
            drop(row,col,board,1)
            if final(board,1):
                print_board(board)
                print("\n\t\t1 wins!!!!")
                break
        turn=2
    else:
        col = int(input("Enter the column no.(2) to put your piece: "))
        if is_empty(board, col):
            row = next_row(board,col)
            drop(row, col, board,2)
            if final(board,2):
                print_board(board)
                print("\n\t\t2 wins!!!!")
                break
        turn=1
    print_board(board)


