from draughts.game import Game


def test_starting_positions():


    target = Game(50)

    result = target.starting_positions(True)
    expected = [(1, 1),(1, 3),(1, 5),(1, 7),(2, 2),(2, 4),(2, 6),(2, 8),(3, 1),(3, 3),(3, 5),(3, 7)]
    assert(result == expected)

    result = target.starting_positions(False)
    expected = [(8, 8),(8, 6),(8, 4),(8, 2),(7, 7),(7, 5),(7, 3),(7, 1),(6, 8),(6, 6),(6, 4),(6, 2)]
    assert(result == expected)


def test_make_pieces():

    target = Game(50)

    result = target.make_pieces(True)
    # Check that the right number of pieces were made:
    assert(len(result) == 12)
    # Check all of the pieces are black:
    for piece in result:
        assert(piece.is_black())