
from draughts.board import board_coordinates, SQUARE_SIZE

def test_board_coordinates():

    horizontal = 1
    vertical = 1
    result = board_coordinates(horizontal, vertical)
    assert(result == (SQUARE_SIZE/2, SQUARE_SIZE/2))

    horizontal = 5
    vertical = 2
    result = board_coordinates(horizontal, vertical)
    assert(result == ((9*SQUARE_SIZE/2), (3*SQUARE_SIZE/2)))

    horizontal = 8
    vertical = 8
    result = board_coordinates(horizontal, vertical)
    assert(result == ((15*SQUARE_SIZE/2), (15*SQUARE_SIZE/2)))

    horizontal = 10
    vertical = 8
    result = board_coordinates(horizontal, vertical)
    # TODO: check that an error is thrown.

    horizontal = 8
    vertical = 12
    result = board_coordinates(horizontal, vertical)
    # TODO: check that an error is thrown.

    horizontal = 0
    vertical = 5
    result = board_coordinates(horizontal, vertical)
    # TODO: check that an error is thrown.
