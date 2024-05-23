HEIGHT = 900 # Can't import from main because main imports board.
SQUARE_SIZE = 100

def border():
    return (HEIGHT - 8*SQUARE_SIZE)/2

def square_colour(horizontal, vertical):
    if ((horizontal + vertical) % 2) == 0:
        return "black"
    return "white"

# Checks that the given square is a valid position on the board.
# Otherwise raises a ValueError.
def check_valid_square(square):
    if not isinstance(square, tuple):
        raise ValueError("Board square must be a tuple.")
    if len(square) != 2:
        raise ValueError("Board square must have length 2.")


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
            if is_valid_square((x, y)):
                ret.add((x, y))
    return ret


def is_valid_square(position):
    return position[0] > 0 and position[0] < 9 and position[1] > 0 and position[1] < 9


# Given a position and a diagonal square next to to the it.
# This funtion returns the next diagonal in the same direction.
# Returns None if they no next diagonal
def next_diagonal(position, diagonal):
    if not diagonal in diagonals(position):
        raise ValueError()
    move = (diagonal[0] - position[0], diagonal[1] - position[1])
    ret = (diagonal[0] + move[0], diagonal[1] + move[1])

    # If the square is off the board, return None.
    if is_valid_square(ret):
        return ret
    return None