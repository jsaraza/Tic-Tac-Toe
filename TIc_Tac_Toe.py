import pygame

class tic_tac_toe:
    
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        