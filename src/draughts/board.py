HEIGHT = 900 # Can't import from main because main imports board.
SQUARE_SIZE = 100

def border():
    return (HEIGHT - 8*SQUARE_SIZE)/2

def square_colour(horizontal, vertical):
    if ((horizontal + vertical) % 2) == 0:
        return "black"
    return "white"

# Returns the (x, y) coordinates of the centre point 
# of a square on the draughts board, given by its
# horizontal and vertical position.
def board_coordinates(horizontal, vertical):
    return (border() + horizontal*SQUARE_SIZE - SQUARE_SIZE/2, HEIGHT - (border() + vertical*SQUARE_SIZE - SQUARE_SIZE/2))

# Returns a set of all squares that are diagonally 
# adjacent to the given position.
def diagonals(position):
    ret = set()
    for x_offset in (-1, 1):
        for y_offset in (-1, 1):
            # Only add diagonals that are on the board.
            x = position[0] + x_offset
            y = position[1] + y_offset
            if x > 0 and x < 9 and y > 0 and y < 9:
                ret.add((x, y))
    return ret