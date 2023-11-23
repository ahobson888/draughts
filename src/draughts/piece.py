from pgzero.builtins import Actor
from draughts.board import SQUARE_SIZE

class Piece(Actor):
    def __init__(self, name, pos):
        super().__init__(name, pos, width = 0.9 * SQUARE_SIZE, height = 0.9 * SQUARE_SIZE)
