import random
import pygame
from .constants import EMPTY

class Opponent:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.create_opponent()

    def create_opponent(self):
        pass

    def make_move(self, color, board, square):
        board.place2(square, color)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('goha/soundeffects/stoneplaced.wav'))

    def gen_random_move(self, color, board):
        if len(board.legal_moves) != 0: # just in case but should never happen
            random_square = board.legal_moves[random.randrange(len(board.legal_moves))]
            self.make_move(color, board, random_square)
            return random_square

    def gen_move(self, color, board):

        # easy difficulty
        if (self.difficulty == 0):
            return self.gen_move_bot0(color, board)

        # normal difficulty
        elif (self.difficulty == 1):
            return self.gen_move_bot1(color, board)

        # hard difficulty
        elif (self.difficulty == 2):
            return None
            # to implement

        # random move
        elif (self.difficulty == 3):
            return self.gen_random_move(color, board)

        # solo
        elif (self.difficulty == 4):
            pass

            # dodac board.restore_board()
    def gen_move_bot0(self, color, board):
        ################################################################################################################
        #
        #    AI logic (first defense, then attack)
        #
        # 1. If opponent's group have only one liberty left then CAPTURE it
        #
        # 2. If the group of the side to move has only one liberty then SAVE it by putting a stone there unless it's a board edge
        #
        # 3. If the group of the side to move has two liberties then DEFEND by choosing the the one resulting in more liberties unless the group will have less than 2 liberties
        #
        # 4. If opponent's group has more than one liberty then try to SURROUND it by placing stone on best liberty
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
                    best_liberty = board.evaluate_0(color)
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
                    best_liberty = board.evaluate_0(3 - color)
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
        return best_move

    def gen_move_bot1(self, color, board):
        ################################################################################################################
        #
        #    AI logic (first defense, then attack)
        #
        # 1. If opponent's group have only one liberty left then CAPTURE it
        #
        # 2. If the group of the side to move has only one liberty then SAVE it by putting a stone there unless: it's a board edge or the group will have less than 2 liberties
        #
        # 3. If the group of the side to move has two liberties then DEFEND by choosing the the one resulting in more liberties unless the group will have less than 2 liberties
        #
        # 4. If opponent's group has more than one liberty then try to SURROUND it unless the placed group will have less than 2 liberties
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
                    board.restore_board()
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
                        best_liberty = board.evaluate_1(color)
                        if best_liberty:
                            save = best_liberty
                            board.restore_board()
                            break
                board.restore_board()

        # defend own group
        for square in range(len(board.board)):
            piece = board.board[square]
            if piece & color:
                board.count(square, color)
                if len(board.liberties) == 2:
                    best_liberty = board.evaluate_1(color)
                    if best_liberty:
                        defend = best_liberty
                        board.restore_board()
                        break
                board.restore_board()

        # surround opponent's group
        for square in range(len(board.board)):
            piece = board.board[square]
            if piece & (3 - color):
                board.count(square, (3 - color))
                if len(board.liberties) > 1:
                    best_liberty = board.evaluate_2(3 - color)
                    if best_liberty:
                        surround = best_liberty
                        board.restore_board()
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
        return best_move