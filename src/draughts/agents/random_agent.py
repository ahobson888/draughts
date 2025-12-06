from draughts.agent import Agent
import random

class RandomAgent(Agent):


    def choose_move(self):
        pieces = self.get_pieces()
        moves = list()
        for piece in pieces:
            taking_moves = self.game.possible_taking_moves(piece)
            if len(taking_moves) == 0:
                continue
            moves.append((piece, random.choice(list(taking_moves))))
        if len(moves) > 0:
            # TODO randomly select a piece and a move in the right way
            return random.choice(list(moves))
        for piece in pieces:
            nontaking_moves = self.game.possible_nontaking_moves(piece)
            if len(nontaking_moves) == 0:
                continue
            moves.append((piece, random.choice(list(nontaking_moves))))
        if len(moves) > 0:
            return random.choice(list(moves))
        return None
    