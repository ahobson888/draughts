from draughts.piece import Piece

def test_diagonals():



    target = Piece("black-piece", (1, 1))
    result = target.diagonals()
    expected = [(2, 2)]
    assert(result == expected)

    target.is_king = True
    result = target.diagonals()
    expected = [(2, 2)]
    assert(result == expected)


    target = Piece("black-piece", (3, 3))
    result = target.diagonals()
    expected = [(2, 4), (4, 4)]
    assert(result == expected)
    
    target.is_king = True
    result = target.diagonals()
    expected = [(2, 2), (4, 2), (2, 4), (4, 4)]
    assert(result == expected)


    target = Piece("black-piece", (8, 2))
    result = target.diagonals()
    expected = [(7, 3)]
    assert(result == expected)
    
    target.is_king = True
    result = target.diagonals()
    expected = [(7, 3), (7, 1)]
    assert(result == expected)


    target = Piece("white-piece", (8, 8))
    result = target.diagonals()
    expected = [(7, 7)]
    assert(result == expected)

    target.is_king = True
    result = target.diagonals()
    expected = [(7, 7)]
    assert(result == expected)


    target = Piece("white-piece", (6, 6))
    result = target.diagonals()
    expected = [(7, 5), (5, 5)]
    assert(result == expected)

    target.is_king = True
    result = target.diagonals()
    expected = [(7, 7), (5, 7), (7, 5), (5, 5)]
    assert(result == expected)


    target = Piece("white-piece", (1, 7))
    result = target.diagonals()
    expected = [(2, 6)]
    assert(result == expected)

    target.is_king = True
    result = target.diagonals()
    expected = [(2, 6), (2, 8)]
    assert(result == expected)