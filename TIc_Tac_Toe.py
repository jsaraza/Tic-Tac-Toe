import pygame

class tic_tac_toe:
    
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.player = "X"

    def click(self, x : int, y :int):
        self.board[x][y] = self.player
        if self.checkWin(x, y):
            return True
        else:
            if self.player == "O":
                self.player = "X"
            else:
                self.player = "O"
    
        return False
        
        

    
    def checkRow(self, row:int):
        counter = 0
        for col in range(3):
            if self.board[row][col] == self.player:
                counter += 1
            else:
                counter = 0
        
        if counter == 3:
             return True
        else:
            return False
    
    def checkHorizontal(self, col: int):
        counter = 0
        for row in range(3):
            if self.board[row][col] == self.player:
                counter+=1
            else:
                counter = 0
        
        if counter == 3:
            return True
        else:
            return False

    def checkDiagonal(self):
        x = 0
        if self.board[x][x] == self.board[x + 1][x + 1] and self.board[x+2][x+2] == self.board[x + 1][x +1]:
            return True
        elif self.board[x+2][x] == self.board[x + 1][x + 1] and self.board[x][x+2] == self.board[x + 1][x + 1]:
            return True
        else: 
            return False


    def checkWin(self, row: int, col: int):
        if self.checkDiagonal():
            return True
        elif self.checkHorizontal(col):
            return True
        elif self.checkRow(row):
            return True
        else:
            return False
