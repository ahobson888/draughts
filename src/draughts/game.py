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

    # Gets the piece in the given position. Returns None if there is no piece in that position.
    def get_piece(self, position):
        for piece in self.black_pieces:
            if piece.position == position:
                return piece
        for piece in self.white_pieces:
            if piece.position == position:
                return piece
        return None


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
                        positions.append((column, row))
                    else:
                        positions.append((9 - column, 9 - row))
        return positions
    

    # Return True if the given square contains a white piece.
    # Otherwise returns False.
    def contains_white_piece(self, square):
        check_valid_square(square)
        for piece in self.white_pieces:
            if piece.position == square:
                return True
        return False


    # Return True if the given square contains a black piece.
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
    

    # Returns True if the given square contains a piece of the same colour as the given piece.
    # Otherwise returns False. 
    def contains_same_colour_piece(self, square, piece):
        if piece.is_black():
            return self.contains_black_piece(square)
        else:
            return self.contains_white_piece(square)


    # Returns True if the given square contains a piece of the opposite colour as the given piece.
    # Otherwise returns False. 
    def contains_opposite_colour_piece(self, square, piece):
        if piece.is_black():
            return self.contains_white_piece(square)
        else:
            return self.contains_black_piece(square)
        


    def possible_moves(self, piece):
        takes = self.possible_taking_moves(piece)
        if len(takes) > 0:
            return takes
        return self.possible_nontaking_moves(piece)
    

    def possible_nontaking_moves(self, piece):
        print(f"piece at: {piece.position}")
        diagonals = piece.diagonal_moves()
        moves = set()
        for diagonal in diagonals:
            print(f"diagonal: {diagonal}")
            if not self.contains_piece(diagonal):
                moves.add((piece.position, diagonal))
        return moves
    

# daddy pseudo code
    def possible_taking_moves(self, piece, current_move=tuple()):
        if len(current_move) == 0:
            # Trailing comma to create a tuple containing one tuple:
            current_move = (piece.position, )
        diagonals = piece.diagonal_moves()
        moves = set()
        for diagonal in diagonals:
            move = current_move
            if self.contains_opposite_colour_piece(diagonal, piece):
                nxt_diagonal = next_diagonal(piece.position, diagonal)
                if self.contains_piece(nxt_diagonal):
                    continue
                # A capture is possible, so update the `move`.
                # Append to a list and then convert back to a tuple.
                l = list(move)
                l.append(nxt_diagonal)
                move = tuple(l)
                # Check whether further captures are possible by constructing
                # a new piece but *without* addding it to the game.
                extra_taking_moves = self.possible_taking_moves(Piece(piece.name(), pos=nxt_diagonal), current_move=move)

                if len(extra_taking_moves) > 0:
                    moves = moves.union(extra_taking_moves)
                else:
                    moves.add(move)
        return moves


    # # Returns a list of possible taking moves (where they are) for the given piece 
    # def allowed_takes(self, piece):

    #     Takes = list()

    #     diagonals = piece.diagonal_moves()

    #     # Loop over each of the possible diagonals, and for each one
    #     # check whether there is a piece that can be taken.
    #     for diagonal in diagonals:
    #         # Check if there is a piece of the opposite colour on this diagonal.
    #         if piece.is_black():
    #             # Chech if there is any piece on the next diaginal square.
    #             # If there isn't the piece can take return Truex
    #             if self.contains_white_piece(diagonal):
    #                 # Chech if there is any piece on the next diaginal square.
    #                 # If there isn't the piece can take return True 
    #                 if self.contains_piece(next_diagonal(piece.position, diagonal)):
    #                     return False
    #                 else:
    #                     return True
    #             else: 
    #                 continue
    #         else:
    #             # Chech if there is any piece on the next diaginal square.
    #             # If there isn't the piece can take return True
    #             if self.contains_black_piece(diagonal):
    #                 if self.contains_piece(next_diagonal(piece.position, diagonal)):
    #                     return False
    #                 else:
    #                     return True
                    
    #     # if no piece was found take can be taken, return False
    #     return False
        


    # Returns True if the piece can take.
    # Returns False if it can't take.
    # def can_take(self, piece):
    #     diagonals = piece.diagonal_moves()

    #     print("CAN TAKE FUNCTION")

    #     # Loop over each of the possible diagonals, and for each one
    #     # check whether there is a piece that can be taken.
    #     for diagonal in diagonals:
    #         # Check if there is a piece of the opposite colour on this diagonal.


    #         # testing:
    #         print("here")
    #         print(piece.position)
    #         print(piece.is_black())
    #         print(diagonal)
    #         print(self.contains_opposite_colour_piece(diagonal, piece))
    #         print("black pieces:")
    #         for p in self.black_pieces:
    #             print(p.position)
    #         print("end of black pieces")

    #         if self.contains_opposite_colour_piece(diagonal, piece):
    #             nxt_diagonal = next_diagonal(piece.position, diagonal)
    #             # Chech if there is any piece on the next diaginal square.
    #             # If there isn't, the piece can take so return True.
    #             # If there is no next diagonal square, or it contains another piece, return False.



    #             if nxt_diagonal is None or self.contains_piece(nxt_diagonal):
    #                 return False
    #             else:
    #                 return True
    #         else: 
    #             continue
    #     # if no piece was found take can be taken, return False
    #     return False

        # diagonals = piece.diagonal_moves()

        # # Loop over each of the possible diagonals, and for each one
        # # check whether there is a piece that can be taken.
        # for diagonal in diagonals:
        #     # Check if there is a piece of the opposite colour on this diagonal.
        #     if piece.is_black():
        #         # Chech if there is any piece on the next diaginal square.
        #         # If there isn't the piece can take return True
        #         if self.contains_white_piece(diagonal):
        #             nxt_diagonal = next_diagonal(piece.position, diagonal)
        #             # Chech if there is any piece on the next diaginal square.
        #             # If there isn't the piece can take return True
        #             # If there is no next diagonal square, or, it contains another piece, return False.
        #             if nxt_diagonal is None or self.contains_piece(nxt_diagonal):
        #                 return False
        #             else:
        #                 return True
        #         else: 
        #             continue
        #     else:
        #         # Chech if there is any piece on the next diaginal square.
        #         # If there isn't the piece can take return True
        #         if self.contains_black_piece(diagonal):
        #             nxt_diagonal = next_diagonal(piece.position, diagonal)
        #             # If there is no next diagonal square, or, it contains another piece, return False.
        #             if nxt_diagonal is None or self.contains_piece(nxt_diagonal):
        #                 return False
        #             else:
        #                 return True
                    
        # # if no piece was found take can be taken, return False
        # return False



    # Returns the set of possible next moves for a given piece.
    def allowed_moves(self, piece):
        moves = {}
        taking_moves = {}
        # First get all the potential moves to an adjacent diagonal square.
        diagonals = piece.diagonal_moves()


        # For each potential move:
        for diagonal in diagonals:
           # If a piece of the same colour is on that square, it's not a valid move.
            if self.contains_same_colour_piece(diagonal, piece):
                continue
            # If a piece of the opposite colour is on that square, we might be able to take it
            if self.contains_opposite_colour_piece(diagonal, piece):
                continue
                # TODO check if the piece can take.
                
            


        # If there are any taking moves, only those moves are allowed:
        if len(taking_moves) > 0:
            return taking_moves
        return moves