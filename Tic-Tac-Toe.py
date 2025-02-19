import pygame
import sys
import TIc_Tac_Toe as TTT
import TictacToeAI as AI

# Initialize Pygame
pygame.init()

board = TTT.tic_tac_toe()


# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
GRID_SIZE = 3  # Size of the grid (3x3 for Tic-Tac-Toe)
LINE_COLOR = (0, 0, 0)  # Color of the grid lines
LINE_WIDTH = 10
CIRCLE_RADIUS = 40


# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe Grid")

font = pygame.font.Font(None, 75)  # None specifies the default system font, and 36 is the font size

# Define the grid lines
GRID_LINE_WIDTH = 5  # Width of the grid lines
line_spacing = SCREEN_WIDTH // GRID_SIZE


def Draw_X(x,y):
    # convert board coordinates to pixel cordinates
    X = x * 100
    Y = y * 100
    pygame.draw.line(screen, LINE_COLOR, (X + 10, Y + 10), (X + 90, Y + 90), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (X + 90, Y + 10), (X + 10, Y + 90), LINE_WIDTH)

def Draw_O(x,y):
    # convert board coordinates to pixel cordinates
    X = x * 100
    Y = y * 100
    pygame.draw.circle(screen, LINE_COLOR, (X + 50, Y + 50), CIRCLE_RADIUS, LINE_WIDTH)


def drawBoard(board:TTT.tic_tac_toe):
    print(board.board)



screen.fill((255, 255, 255))

turn = False

# Main game loop
running = True
gameIsWon = False
numOfSquares = 0
while running:

    if board.player == "O":
        gameIsWon = AI.list_random_move(board)
        


    # Clear the screen
    #screen.fill((255, 255, 255))
    # Draw horizontal grid lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, i * line_spacing), (SCREEN_WIDTH, i * line_spacing), GRID_LINE_WIDTH)

    # Draw vertical grid lines
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * line_spacing, 0), (i * line_spacing, SCREEN_HEIGHT), GRID_LINE_WIDTH)

    # Get mouse pos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and gameIsWon == False and numOfSquares < 9:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Gets corrdinates of mouse click on board
            cor_X = mouse_x // 100
            cor_Y = mouse_y // 100
            numOfSquares += 1
            if board.click(cor_X, cor_Y):
                gameIsWon = True
                print(board.player + " won!")



    # Draw board based on board object
    for row in range(0,3):
        for col in range(0,3):
            letter = board.board[row][col]
            if letter == "X":
                Draw_X(row,col)
            elif letter == "O":
                Draw_O(row,col)

    if numOfSquares == 9:
        text = font.render("Tie!", True, (255, 100, 0))
        screen.blit(text, (110, 120))

    # Displays winning message if player won
    if gameIsWon == True:
        text = font.render(board.player + " won!", True, (255, 100, 0))
        screen.blit(text, (70, 120))

    
            
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
