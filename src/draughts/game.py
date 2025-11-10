from draughts.piece import Piece
from draughts.board import check_valid_square, next_diagonal
import random
from sys import exit



class Game():


    def __init__(self):
        self.black_pieces = []
        self.white_pieces = []

        
    def start(self):
        # Game has two list of pieces.
        self.black_pieces = self.make_pieces(True)
        self.white_pieces = self.make_pieces(False)


    # Plays a move and stops it if the game has finished
    # and True if the game has finished.
    def play_move(self, is_black):
        if is_black:
            move = self.choose_move(self.black_pieces)
        else:
            move = self.choose_move(self.white_pieces)
        # If no move is possible, the game is drawn.
        if move is None:
            print("It was a draw.") 
            exit()
        # Move the piece and check whether the game is finished.
        self.move_piece(move)
        if len(self.black_pieces) == 0:
            print("The winner is white!")
            exit()
        if len(self.white_pieces) == 0:
            print("The winner is black!")
            exit()
        

    def move_piece(self, move):
        # First get the piece that is going to move.
        piece = move[0]
        squares = move[1]
        if piece is None:
            print("Error invalid move, no piece at starting position")
            exit()
        # Change the position of the piece to the next element then see if it needs to move again.
        piece.change_position(squares[1])
        # If a taking move remove the taken piece.
        pos0 = squares[0]
        pos1 = squares[1]
        diff = tuple(abs(x - y) for x, y in  zip(pos0, pos1))
        if diff == (2, 2):
            taken_piece = self.get_piece(self.taken_position(squares[:2]))
            if taken_piece is None:
                print("There is no piece to take.")
                exit()
            # Remove taken piece from Game.
            self.remove_piece(taken_piece)
        # If the piece has reach the end of the board, turn it into a king 
        if piece.is_on_king_rank():
            piece.is_king = True
        # If there are more jumps in this move, called this method recursively.  
        if len(squares) > 2:
            self.move_piece((piece, squares[1:]))

    def taken_position(self, jump):
        print(f"jump: {jump}")
        col0 = jump[0][0]
        col1 = jump[1][0]
        row0 = jump[0][1]
        row1 = jump[1][1]
        if col1 > col0:
            col = col0 + 1
        else:
            col = col0 - 1
        if row1 > row0:
            row = row0 + 1
        else:
            row = row0 - 1
        return (col, row)
    
    def remove_piece(self, piece):
        if piece.is_black():
            self.black_pieces.remove(piece)
        else:
            self.white_pieces.remove(piece)

    # Returns a piece and a possible move in a tuple starting with the taking moves then the nontaking moves.
    def choose_move(self, pieces):
        moves = list()
        for piece in pieces:
            taking_moves = self.possible_taking_moves(piece)
            if len(taking_moves) == 0:
                continue
            moves.append((piece, random.choice(list(taking_moves))))
        if len(moves) > 0:
            # TODO randomly select a piece and a move in the right way
            return random.choice(list(moves))
        for piece in pieces:
            nontaking_moves = self.possible_nontaking_moves(piece)
            if len(nontaking_moves) == 0:
                continue
            moves.append((piece, random.choice(list(nontaking_moves))))
        if len(moves) > 0:
            move = random.choice(list(moves))
            print("Chosen move")
            print(move)
            return move
        return None

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
        

    # Returns the set of possible moves for the given piece.
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
                if nxt_diagonal is None:
                    continue
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