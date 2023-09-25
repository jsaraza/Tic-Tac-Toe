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

    def checkDiagonalLeft(self):
        counter = 0
        
        for i in range(3):
            if self.board[i][2-i] == self.player:
                counter +=1
            else:
                counter = 0
                
        for j in range(3):
            if self.board[i][i] == self.player:
                counter +=1 
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
