import pgzrun
from draughts.board import square_colour, board_coordinates, SQUARE_SIZE
from draughts.game import Game

# Canvas size:
WIDTH = 900
HEIGHT = 900

def draw():
    screen.clear()
    screen.fill("dark orange")
    border = SQUARE_SIZE/2
    draw_board(border)
    game = Game(border)
    start(game)
    return

# Draws the draughts board.
def draw_board(border):
    for h in range(1, 9):
        for v in range(1, 9):
            colour = square_colour(h, v)
            draw_square(board_coordinates(h, v, border), colour)
    return 

# Draws a square at the centre coordinates.
def draw_square(centre, colour):
    global SQUARE_SIZE
    top_left = (centre[0]-(SQUARE_SIZE/2), centre[1]-(SQUARE_SIZE/2))
    box = Rect(top_left, (SQUARE_SIZE, SQUARE_SIZE))
    screen.draw.filled_rect(box, colour)
    centre[0]-(SQUARE_SIZE/2)
    centre[1]-(SQUARE_SIZE/2)
    centre[0]+(SQUARE_SIZE/2)
    centre[1]+(SQUARE_SIZE/2)

def start(game):
    game.start()
    game.draw_pieces()

pgzrun.go()