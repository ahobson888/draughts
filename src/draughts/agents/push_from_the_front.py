from draughts.agent import Agent
import random


class PushFromTheFront(Agent):
        

    def choose_move(self):
        # Find the piece at the front (taking into acount if you are black or white) that has a taking move
        # If there is more than one chose one at random
        # If there is none find the piece at the front (taking into acount if you are black or white) that has a non-taking move 
        # Then get the move

        # Get the set of all possible taking moves (with the relevant piece at index 0 of the tuple).
        all_taking_moves = self.game.all_taking_moves(self.get_pieces())
        # Find the front-most piece(s) that can make a taking move.
        if len(all_taking_moves) > 0:
            ranks = {m[0].rank() for m in all_taking_moves}
            if self.is_black:
                top_rank = max(ranks)
            else:
                top_rank = min(ranks)
            moves = {m for m in all_taking_moves if m[0].rank() == top_rank}
            return random.choice(list(moves))
        # If there are no taking moves get the set of all possible nontaking moves (with the relevant piece at index 0 of the tuple). 
        nontaking_moves = self.game.all_nontaking_moves(self.get_pieces(), False)
        # Find the front-most piece(s) that can make a move.
        if len(nontaking_moves) > 0:
            ranks = {m[0].rank() for m in nontaking_moves}
            if self.is_black:
                top_rank = max(ranks)
            else:
                top_rank = min(ranks)
            moves = {m for m in nontaking_moves if m[0].rank() == top_rank}
            return random.choice(list(moves))
        all_nontaking_moves = self.game.all_nontaking_moves(self.get_pieces(), True)
        if len(all_nontaking_moves) > 0:
            return random.choice(list(all_nontaking_moves))
        return None


        
    #     pieces = self.get_pieces()
    #     moves = list()
    #     # Find the rank of the front-most piece.
    #     max_rank = 0
    #     for piece in pieces:
    #         # taking_moves = self.game.possible_taking_moves(piece)
    #         if len(taking_moves) == 0:
    #             continue
    #         rank = taking_moves[0].rank()
    #         if rank > max_rank:
    #             max_rank = rank
    #     for piece in pieces:
    #         if piece[1] == max_rank:
    #             moves.append(piece)
    #             return random.choice(moves)
    #     else:
    #         for nontaking_moves in pieces:
    #             nontaking_moves = self.game.possible_nontaking_moves(piece)
    #             rank = nontaking_moves[0][1]
    #             if rank > max_rank:
    #                 max_rank = rank
    #             for piece in pieces:
    #                 if piece[1] == max_rank:
    #                     moves.append(piece)
    #                     if len(moves) > 0:
    #                         return random.choice(moves)
    #                     return None
                    
    # def choose_move_white(self):
            
        
    #     min_rank = 9
    #     moves = list()
    #     pieces = self.get_pieces(False)

    #     for taking_moves in pieces:
    #         taking_moves = self.game.possible_taking_moves(piece)
    #         if len(taking_moves) == 0:
    #             continue
    #         rank = taking_moves[0][1]
    #         if rank < min_rank:
    #             min_rank = rank
    #         for piece in pieces:
    #             if piece[1] == min_rank:
    #                 moves.append(piece)
    #                 return random.choice(moves)
    #     else:
    #         for nontaking_moves in pieces:
    #             nontaking_moves = self.game.possible_nontaking_moves(piece)
    #             rank = nontaking_moves[0][1]
    #             if rank < min_rank:
    #                 min_rank = rank
    #             for piece in pieces:
    #                 if piece[1] == min_rank:
    #                     moves.append(piece)
    #                     if len(moves) > 0:
    #                         return random.choice(moves)
    #                     return None
                    
    # def choose_move(self, is_black):
    #     if is_black:
    #         return self.choose_move_black()
    #     else:
    #         return self.choose_move_white()