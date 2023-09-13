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

    def gen_random_move(self, color, board):
        if len(board.legal_moves) != 0: # just in case but should never happen
            random_square = board.legal_moves[random.randrange(len(board.legal_moves))]
            return random_square

    def gen_move(self, color, board):
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
        
        # capture opponent's group
        for square in range(len(board.board)):
            piece = board.board[square]
            if piece & (3 - color):
                board.count(square, (3 - color))
                if len(board.liberties) == 1 and (board.liberties[0] in board.legal_moves):
                    target_square = board.liberties[0]
                    capture = target_square
                    break
                board.restore_board()

        # save own group
        for square in range(len(board.board)):
            piece = board.board[square]
            if piece & (color):
                board.count(square, (color))
                if len(board.liberties) == 1 and (board.liberties[0] in board.legal_moves):
                    target_square = board.liberties[0]
                    if not board.detect_edge(target_square):
                        save = target_square
                        break
                board.restore_board()

        # defend own group
        for square in range(len(board.board)):
            piece = board.board[square]
            if piece & color:
                board.count(square, color)
                if len(board.liberties) == 2:
                    best_liberty = board.evaluate(color)
                    if best_liberty:
                        defend = best_liberty
                        break
                board.restore_board()

        # surround opponent's group
        for square in range(len(board.board)):
            piece = board.board[square]
            if piece & (3 - color):
                board.count(square, (3 - color))
                if len(board.liberties) > 1:
                    best_liberty = board.evaluate(3 - color)
                    if best_liberty:
                        surround = best_liberty
                        break
                board.restore_board()

        if capture:
            print('capture move')
            best_move = capture
        elif save:
            print('save move')
            best_move = save
        elif defend:
            print('defend move')
            best_move = defend
        elif surround:
            print('surround move')
            best_move = surround
        else:
            print('random move')
            best_move = self.gen_random_move(color, board)

        self.make_move(color, board, best_move)