from draughts.piece import Piece
from draughts.board import check_valid_square, next_diagonal



class Game():


    def __init__(self):
        self.black_pieces = []
        self.white_pieces = []

        
    def start(self):
        # Game has two list of pieces.
        self.black_pieces = self.make_pieces(True)
        self.white_pieces = self.make_pieces(False)

    # Make all the pieces. 
    # Returns a list of pieces.
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
    

    # Return True if the given square contains and white piece.
    # Otherwise returns False.
    def contains_white_piece(self, square):
        check_valid_square(square)
        for piece in self.white_pieces:
            if piece.position == square:
                return True
        return False


    # Return True if the given square contains and black piece.
    # Otherwise returns False.
    def contains_black_piece(self, square):
        check_valid_square(square)
        for piece in self.black_pieces:
            if piece.position == square:
                return True
        return False
    

    def contains_piece(self, square):
        if square == None:
            return False
        return self.contains_black_piece(square) or self.contains_white_piece(square)



    # Returns True if the piece can take.
    # Returns False if it can't take.e):
    def can_take(self, piece):
        diagonals = piece.diagonal_moves()

        # Loop over each of the possible diagonals, and for each one
        # check whether there is a piece that can be taken.
        for diagonal in diagonals:
            # Check if there is a piece of the opposite colour on this diagonal.
            if piece.is_black():
                # Chech if there is any piece on the next diaginal square.
                # If there isn't the piece can take return True
                if self.contains_white_piece(diagonal):
                    if self.contains_piece(next_diagonal(piece.position, diagonal)):
                        return False
                    else:
                        return True
                    # Chech if there is any piece on the next diaginal square.
                    # If there isn't the piece can take return True
                else: 
                    continue
            else:
                # Chech if there is any piece on the next diaginal square.
                # If there isn't the piece can take return True
                if self.contains_black_piece(diagonal):
                    if self.contains_piece(next_diagonal(piece.position, diagonal)):
                        return False
                    else:
                        return True
                    
        # if no piece was found take can be taken, return False
        return False


    # Returns the set of possible next moves for a given piece.
    def allowed_moves(self, piece):
        moves = {}
        taking_moves = {}
        # First get all the potential moves to an adjacent diagonal square.
        diagonals = piece.diagonal_moves()

        # For each potential move:
        for diagonal in diagonals:
           # If a piece of the same colour is on that square, it's not a valid move.
            if piece.is_black():
                if self.contains_black_piece(diagonal):
                    continue
                if self.contains_white_piece(diagonal):
                    # TODO: need to check if the diagonal square beyond the white piece is empty. 
                    continue


        # If there are any taking moves, only those moves are allowed:
        if len(taking_moves) > 0:
            return taking_moves
        return moves