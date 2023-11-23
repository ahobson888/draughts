from draughts.piece import Piece
from draughts.board import board_coordinates

class Game():
    def __init__(self, border) -> None:
        self.border = border
        # Game has a list of pieces.
        # self.pieces = self.make_pieces()

    def make_pieces(self):
        # TODO: make all of the pieces, not just one.
        return [Piece("white-piece", board_coordinates(1, 1, self.border))]
    
    def draw_pieces(self):
        for piece in self.pieces:
            piece.draw()
    
    # Returs a list of starting positions for 1 colour of pieces
    def starting_positions(self, is_black):
        # TODO
        return [(1, 1),(1, 3)]