import pgzrun

WIDTH = 1000
HEIGHT = 1000
SQUARE_SIZE = 100

def draw_square(centre, colour):
    global SQUARE_SIZE
    top_left = (centre[0]-(SQUARE_SIZE/2),centre[1]-(SQUARE_SIZE/2))
    box = Rect(top_left, (SQUARE_SIZE, SQUARE_SIZE))
    screen.draw.filled_rect(box, colour)
    centre[0]-(SQUARE_SIZE/2)
    centre[1]-(SQUARE_SIZE/2)
    centre[0]+(SQUARE_SIZE/2)
    centre[1]+(SQUARE_SIZE/2)

# Returns the (x, y) coordinates of the centre point 
# of a square on the draughts board, given by its
# horizontal and vertical position.
def board_coordinates(horizontal, vertical):
    # todo
    return (0, 100)

