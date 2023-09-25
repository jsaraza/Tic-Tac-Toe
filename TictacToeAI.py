import TIc_Tac_Toe as TTT
import random


def list_random_move(board:TTT.tic_tac_toe):

    moves = []


    for row in range(3):
        for col in range(3):
           if board.board[row][col] == " ":
                moves.append((row,col))

    if len(moves) > 1:
        coordinate_x, coordinate_y = random.choice(moves)
        return board.click(coordinate_x, coordinate_y)

    return False


