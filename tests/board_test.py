from draughts.board import *
import pytest

def test_board_coordinates():

    horizontal = 1
    vertical = 1
    result = board_coordinates(horizontal, vertical)
    assert(result == (50 + SQUARE_SIZE/2,  HEIGHT - (50 + SQUARE_SIZE/2)))

    horizontal = 5
    vertical = 2
    result = board_coordinates(horizontal, vertical)
    assert(result == ((50 + 9*SQUARE_SIZE/2), HEIGHT - (50 + 3*SQUARE_SIZE/2)))

    horizontal = 8
    vertical = 8
    result = board_coordinates(horizontal, vertical)
    assert(result == ((50 + 15*SQUARE_SIZE/2), HEIGHT - (50 + 15*SQUARE_SIZE/2)))

    # with pytest.raises(ValueError):
    #     horizontal = 10
    #     vertical = 8
    # TODO: check that an error is thrown.

    # with pytest.raises(ValueError):
    #     horizontal = 8
    #     vertical = 12
    # # TODO: check that an error is thrown.

    # with pytest.raises(ValueError):
    #     horizontal = 0
    #     vertical = 5
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

    # with pytest.raises(ValueError):
    #     horizontal = 10
    #     vertical = 8
    # TODO: check that an error is thrown.



def test_next_diagonal():

    # The test will not fall ,because next_diagonal has a yellow line under it 
    # It might fall because the funtion is not working.
    result = next_diagonal((1, 1), (2, 2))
    assert(result == (3, 3))

    result = next_diagonal((6, 6), (7, 7))
    assert(result == (8, 8))

    result = next_diagonal((5, 5), (4, 6))
    assert(result == (3, 7))

    result = next_diagonal((2, 7, ), (1, 8, ))
    assert(result == None)

    result = next_diagonal((8, 4), (7, 3))
    assert(result == (6, 2))

    with pytest.raises(ValueError):
        next_diagonal((4, 2), (7, 8))