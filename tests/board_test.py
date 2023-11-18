
from draughts.board import *

def test_board_coordinates():

    border = 50
    horizontal = 1
    vertical = 1
    result = board_coordinates(horizontal, vertical, border)
    assert(result == (50 + SQUARE_SIZE/2, 50 + SQUARE_SIZE/2))

    horizontal = 5
    vertical = 2
    result = board_coordinates(horizontal, vertical, border)
    assert(result == ((50 + 9*SQUARE_SIZE/2), (50 + 3*SQUARE_SIZE/2)))

    horizontal = 8
    vertical = 8
    result = board_coordinates(horizontal, vertical, border)
    assert(result == ((50 + 15*SQUARE_SIZE/2), (50 + 15*SQUARE_SIZE/2)))

    horizontal = 10
    vertical = 8
    result = board_coordinates(horizontal, vertical, border)
    # TODO: check that an error is thrown.

    horizontal = 8
    vertical = 12
    result = board_coordinates(horizontal, vertical, border)
    # TODO: check that an error is thrown.

    horizontal = 0
    vertical = 5
    result = board_coordinates(horizontal, vertical, border)
    # TODO: check that an error is thrown.

def test_square_colour():

    horizontal = 1
    vertical = 1
    result = square_colour(horizontal, vertical)
    assert(result == "black")

    horizontal = 8
    vertical = 1
    result = square_colour(horizontal, vertical)
    assert(result == "white")

    horizontal = 5
    vertical = 7
    result = square_colour(horizontal, vertical)
    assert(result == "black")

    horizontal = 4
    vertical = 5
    result = square_colour(horizontal, vertical)
    assert(result == "white")

    horizontal = 10
    vertical = 8
    result = square_colour(horizontal, vertical)
    # TODO: check that an error is thrown.
