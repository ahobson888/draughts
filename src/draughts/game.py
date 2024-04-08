from draughts.piece import Piece

class Game():
    # def __init__(self, border) -> None:
    #     self.border = border

    def start(self):
        # Game has two list of pieces.
        self.black_pieces = self.make_pieces(True)
        self.white_pieces = self.make_pieces(False)

    # make all the pieces. 
    # returns a list of pieces.
    def make_pieces(self, is_black):
        start_positions = self.starting_positions(is_black)
        pieces = []
        for pos in start_positions:
            pieces.append(Piece(self.piece_name(is_black), pos))
        return pieces
    
    def piece_name(self, is_black):
        if is_black:
            return "black-piece"
        return "white-piece"

    def draw_pieces(self):
        for piece in self.black_pieces:
            piece.draw()
        for piece in self.white_pieces:
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
    

    def contains_white_piece(self, square):
        for piece in self.white_pieces:
            if piece.position == square:
                return True
        return False


    def contains_black_piece(self, square):
        for piece in self.black_pieces:
            if piece.position == square:
                return True
        return False

        
    # Returns the set of possible next moves for a given piece.
    def allowed_moves(self, piece):
        # if piece.is_king:
            
        # is it king?
        moves = {}
        # TODO.
        return moves