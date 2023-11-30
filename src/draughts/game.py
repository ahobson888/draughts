from draughts.piece import Piece
from draughts.board import board_coordinates

class Game():
    def __init__(self, border) -> None:
        self.border = border

    def start(self, is_black):
        # Game has a list of pieces.
        self.pieces = self.make_pieces()

    # make all the pieces. 
    # returns a list of pieces.
    def make_pieces(self, is_black):
        

        return []
        # TODO: make all of the pieces, not just one.
        # return [Piece("white-piece", board_coordinates(1, 1, self.border))]
    
    def draw_pieces(self):
        for piece in self.pieces:
            piece.draw()
    
    # Returns a list of starting positions for 1 colour of pieces
    def starting_positions(self, is_black):
        positions = []
        for row in range(1, 4):
            for column in range(1, 9):
                if ((row + column) % 2) == 0:
                    if is_black:
                        positions.append((row, column))
                    else:
                        positions.append((9 - row, 9 - column))
        return positions
        