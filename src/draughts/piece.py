from pgzero.builtins import Actor
from draughts.board import board_coordinates
from draughts.board import SQUARE_SIZE

class Piece(Actor):
    def __init__(self, name, pos):
        print(f"New {name} at {pos}")
        # Use the position attribute to keep track of the board square
        # that this piece is on.
        self.position = pos
        # Use the is_king attibute to keep track of whether this piece is a king.
        self.is_king = False
        # Compute the pixel coordinates from the board square:
        coords = board_coordinates(pos[1], pos[0])
        super().__init__(name, coords, width = 0.9 * SQUARE_SIZE, height = 0.9 * SQUARE_SIZE)
        

    def name(self):
        return self._image_name

    # Returns True if the this piece is black
    # Returns False if the this piece is white 
    def is_black(self):
        if self.name() == "black-piece":
            return True
        else:
            return False
        
    # Returns the list of (one, two or four) diagonal squares that a 
    # piece could move to if there are no other pieces nearby.
    def diagonal_moves(self):
        moves = []
        # TODO
        return moves