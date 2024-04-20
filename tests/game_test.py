from draughts.game import Game
import pygame

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

