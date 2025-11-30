

class Agent:

    def __init__(self, game, is_black):
        self.game = game
        self.is_black = is_black


    # Returns a piece and a possible move in a tuple starting with the taking moves then the nontaking moves.
    def choose_move(self):
        raise NotImplementedError()
    
    
    
    def get_pieces(self):
        if self.is_black:
            return self.game.black_pieces
        return self.game.white_pieces 
  