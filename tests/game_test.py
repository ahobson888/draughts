from draughts.game import Game
from draughts.piece import Piece
import pygame
import pytest



def test_starting_positions():


    target = Game()

    result = target.starting_positions(True)
    expected = [(1, 1),(1, 3),(1, 5),(1, 7),(2, 2),(2, 4),(2, 6),(2, 8),(3, 1),(3, 3),(3, 5),(3, 7)]
    assert(result == expected)

    result = target.starting_positions(False)
    expected = [(8, 8),(8, 6),(8, 4),(8, 2),(7, 7),(7, 5),(7, 3),(7, 1),(6, 8),(6, 6),(6, 4),(6, 2)]
    assert(result == expected)


def test_make_pieces():

    # Initialise pygame, to avoid the error:
    # pygame.error: cannot convert without pygame.display initialized
    
    pygame.init() 
    pygame.display.set_mode((1024, 768))

    target = Game()
    
    result = target.make_pieces(True)
    # Check that the right number of pieces were made:
    assert(len(result) == 12)
    # Check all of the pieces are black:
    for piece in result:
        assert(piece.is_black())

    result = target.make_pieces(False)
    # Check that the right number of pieces were made:
    assert(len(result) == 12)
    # Check all of the pieces are white:
    for piece in result:
        assert(not piece.is_black())


def test_contains_white_piece():


    target = Game()

    assert(not target.contains_white_piece((8, 8)))
    target.white_pieces = target.make_pieces(False)
    assert(target.contains_white_piece((8, 8)))
    assert(not target.contains_white_piece((8, 7)))
    assert(target.contains_white_piece((7, 7)))
    assert(not target.contains_white_piece((7, 6)))
    assert(target.contains_white_piece((6, 6)))
    assert(not target.contains_white_piece((6, 5)))

    # Test for invalid square argument.
    with pytest.raises(ValueError):
        target.contains_black_piece((3, ))
    with pytest.raises(ValueError):
        target.contains_black_piece((3, 4, 5))

def test_contains_black_piece():

    target = Game()

    assert(not target.contains_black_piece((1, 1)))
    target.black_pieces = target.make_pieces(True)
    assert(target.contains_black_piece((1, 1)))
    assert(not target.contains_black_piece((1, 2)))
    assert(target.contains_black_piece((2, 2)))
    assert(not target.contains_black_piece((2, 3)))
    assert(target.contains_black_piece((3, 3)))
    assert(not target.contains_black_piece((3, 4)))

def test_can_take():

    target = Game()

    black44 = Piece("black-piece", (4, 4))
    white55 = Piece("white-piece", (5, 5))
    black11 = Piece("black-piece", (1, 1))
    

    target.black_pieces = [black44, black11]
    target.white_pieces = [white55]


    assert(target.can_take(black44))
    assert(target.can_take(white55))
    assert(not target.can_take(black11))

    white22 = Piece("white-piece", (2, 2))

    
    target.white_pieces.append(white22)

    assert(target.can_take(black11))
    assert(not target.can_take(white22))

    black33 = Piece("black-piece", (3, 3))

    target.black_pieces.append(black33)

    assert(not target.can_take(black11))
    assert(not target.can_take(black33))
    assert(not target.can_take(white22))
    assert(not target.can_take(white55))
    assert(target.can_take(black44))
    
    black13 = Piece("black-piece", (1, 3))

    target.black_pieces.append(black13)

    assert(not target.can_take(black13))

    black13.is_king = True

    assert(target.can_take(black13))

def test_allowed_moves_starting_positions():

    target = Game()
    # Make the pieces in their starting positions.
    target.start()

    piece = target.get_piece((3, 5))
    assert(target.allowed_moves(piece) == {(4, 4), (4, 6)})

    piece = target.get_piece((6, 4))
    assert(target.allowed_moves(piece) == {(5, 3), (5, 5)})

    piece = target.get_piece((7, 5))
    assert(target.allowed_moves(piece) == {})

    piece = target.get_piece((6, 8))
    assert(target.allowed_moves(piece) == {(5, 7)})

    piece = target.get_piece((1, 1))
    assert(target.allowed_moves(piece) == {})

    piece = target.get_piece((3, 1))
    assert(target.allowed_moves(piece) == {(4, 2)})

    # TODO: Add tests about if the piece or king can take. 

def test_allowed_moves_kings():

    target = Game()

    piece = Piece("white-piece", (4, 4))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(3, 3), (5, 3), (3, 5), (5, 5)})

    piece = Piece("white-piece", (5, 5))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(5, 4), (4, 5), (6, 6)})

    piece = Piece("white-piece", (1, 1))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(2, 2)})

    piece = Piece("white-piece", (5, 1))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(6, 2), (4, 2)})

    piece = Piece("white-piece", (7, 7))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(8, 8), (8, 6), (6, 8), (6, 6)})

    piece = Piece("white-piece", (8, 8))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {})

    piece = Piece("white-piece", (2, 2))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(3, 3), (1, 3), (3, 1)})

    piece = Piece("white-piece", (3, 1))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(4, 2)})

    piece = Piece("white-piece", (1, 3))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(2, 4)})

    target = Game()

    piece = Piece("black-piece", (4, 4))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(3, 3), (5, 3), (3, 5), (5, 5)})

    piece = Piece("black-piece", (5, 5))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(5, 4), (4, 5), (6, 6)})

    piece = Piece("black-piece", (1, 1))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(2, 2)})

    piece = Piece("black-piece", (5, 1))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(6, 2), (4, 2)})

    piece = Piece("black-piece", (7, 7))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(8, 8), (8, 6), (6, 8), (6, 6)})

    piece = Piece("black-piece", (8, 8))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {})

    piece = Piece("black-piece", (2, 2))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(3, 3), (1, 3), (3, 1)})

    piece = Piece("black-piece", (3, 1))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(4, 2)})

    piece = Piece("black-piece", (1, 3))
    piece.is_king = True
    assert(target.allowed_moves(piece) == {(2, 4)})

