
# Canvas size:
WIDTH = 900
HEIGHT = 900

SQUARE_SIZE = 100

def square_colour(horizontal, vertical):
    if ((horizontal + vertical) % 2) == 0:
        return "black"
    return "white"

# Returns the (x, y) coordinates of the centre point 
# of a square on the draughts board, given by its
# horizontal and vertical position.
def board_coordinates(horizontal, vertical, border):
    return (border + horizontal*SQUARE_SIZE - SQUARE_SIZE/2,HEIGHT - (border + vertical*SQUARE_SIZE - SQUARE_SIZE/2))
