import pygame, random
from .constants import ROWS, COLS, EMPTY

class Opponent:
    def __init__(self):
        self.difficulty = 0
        self.create_opponent()

    def create_opponent(self):
        pass

    def make_move(self, color, board, square):
        board.place2(square, color)

    def make_random_move(self, color, board):
        if len(board.legal_moves) != 0: # just in case but should never happen
            random_square = board.legal_moves[random.randrange(len(board.legal_moves))]
            self.make_move(color, board, random_square)
    
    def genmove(self, color, board):
        ################################################################################################################
        #
        #    AI logic (first defense, then attack)
        #
        # 1. If opponent's group have only one liberty left then CAPTURE it
        #
        # 2. If the group of the side to move has only one liberty then SAVE it by putting a stone there unless it's a board edge
        #
        # 3. If the group of the side to move has two liberties then DEFEND  BY choosing the the one resulting in more liberties
        #
        # 4. If opponent's group has more than one liberty then try to SURROUND it
        #
        # 5. Match patterns to build strong shape, if found any consider that instead of chasing the group
        #
        ################################################################################################################

        best_move = 0
        capture = 0
        save = 0
        defend = 0
        surround = 0
        
        # defend own group
        for square in range(len(board.board)):
            piece = board.board[square]
            # match own group
            if piece & color:
                # count liberties for own group
                board.count(square, (color))
                # if group has 2 liberties
                if len(board.liberties) == 2:
                    # store the save move
                    best_liberty = board.evaluate(color)
                    best_move = best_liberty
                    defend = best_liberty
                    break
                # restore board
                board.restore_board()
        # found move
        if best_move:
            print('defend move')
            self.make_move(color, board, best_move)
        else:
            self.make_random_move(color, board)
