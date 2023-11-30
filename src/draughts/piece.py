from pgzero.builtins import Actor
from draughts.board import SQUARE_SIZE


class Piece(Actor):
    def __init__(self, name, pos):
        super().__init__(name, pos, width = 0.9 * SQUARE_SIZE, height = 0.9 * SQUARE_SIZE)
        

    # Returns True if the this piece is black
    # Returns False if the this piece is white 
    def is_bLack(self):
        if self.name == "black-piece":
            return True
        else:
            return False