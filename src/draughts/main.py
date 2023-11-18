import pgzrun
from board import square_colour, board_coordinates, SQUARE_SIZE

WIDTH = 900
HEIGHT = 900

def draw():
    screen.clear()
    screen.fill("dark orange")
    draw_board(SQUARE_SIZE/2)
    # draw_square((98654,4543),"black")
    # draw_square((859483,549538),"white")
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

pgzrun.go()
