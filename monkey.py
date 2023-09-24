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


running = True
current_player = 'X'

def draw_board():
    # Implement code to draw the Tic-Tac-Toe board
    pass

def check_winner(player):
    # Implement the logic to check if a player has won
    pass

def check_draw():
    # Implement the logic to check if the game is a draw
    pass


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Implement code to handle player's moves
            pass

    screen.fill(white)
    draw_board()

    if check_winner(current_player):
        # Implement code to display the winner
        pass
    elif check_draw():
        # Implement code to display a draw
        pass

    pygame.display.flip()

pygame.quit()





print("hello world")