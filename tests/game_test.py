from draughts.game import Game


def test_starting_positions():


    target = Game(50)

    result = target.starting_positions(True)
    expected = [(1, 1),(1, 3),(1, 5),(1, 7),(2, 2),(2, 4),(2, 6),(2, 8),(3, 1),(3, 3),(3, 5),(3, 7)]
    assert(result == expected)

    result = target.starting_positions(False)
    expected = ((8, 1),(8, 3),(8, 5),(8, 7),(7, 2),(7, 4),(7, 6),(7, 8),(6, 1),(6, 3),(6, 5),(6, 7))
    assert(result == expected)