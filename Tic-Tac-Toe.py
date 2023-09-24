import pygame
import pygame
pygame.init()
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic-Tac-Toe")

white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 36)

board = [['' for _ in range(3)] for _ in range(3)]



