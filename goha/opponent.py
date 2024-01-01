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
        
    def gen_random_move_bot1(self, color, board):
        considered_moves = [element for element in board.legal_moves if element not in board.territory[color]]
        considered_moves_copy = considered_moves.copy()
        board.restore_board()
        for move in considered_moves:
            board.board[move] = color
            board.count(move, color)
            if len(board.liberties) < 2:
                considered_moves_copy.remove(move)
            board.restore_board()
            board.board[move] = EMPTY
        if len(considered_moves_copy) != 0:
            random_square = considered_moves_copy[random.randrange(len(considered_moves_copy))]
            self.make_move(color, board, random_square)
            print('random move')
            return random_square
        else:
            print('pass move')
            return None 

    def gen_move(self, color, board, game):

        # easy difficulty
        if (self.difficulty == 0):
            return self.gen_move_bot0(color, board)

        # normal difficulty
        elif (self.difficulty == 1):
            return self.gen_move_bot1(color, board)

        # hard difficulty
        elif (self.difficulty == 2):
            return self.gen_move_bot3(color, board, game)
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
        # 3. If the group of the side to move has two liberties then DEFEND by choosing the the one resulting in more liberties
        #
        # 4. If opponent's group has more than one liberty then try to SURROUND it by placing stone on best liberty
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
                    best_liberty = board.evaluate_bot0(color)
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
                    best_liberty = board.evaluate_bot0(3 - color)
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

        if best_move != None:
            self.make_move(color, board, best_move)

        return best_move

    def gen_move_bot1(self, color, board):
        ################################################################################################################
        #
        #    AI logic (first defense, then attack)
        #
        # 1. If opponent's group have only one liberty left then CAPTURE it
        #
        # 2. If the group of the side to move has only one liberty then SAVE it by putting a stone there unless: the group will have less than 2 liberties
        #
        # 3. If the group of the side to move has two liberties then DEFEND by choosing the the one resulting in more liberties unless: the group will have less than 2 liberties
        #
        # 4. If opponent's group has more than one liberty then try to SURROUND it unless the placed group will have less than 2 liberties
        #
        # 5. Else RANDOM move unless: placed on your own territory OR the group will have less than 2 liberties
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
                board.count(square, color)
                if len(board.liberties) == 1 and (board.liberties[0] in board.legal_moves):
                    best_liberty = board.evaluate_bot1_1(color)
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
                    best_liberty = board.evaluate_bot1_1(color)
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
                    best_liberty = board.evaluate_bot1_2(3 - color)
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
            best_move = self.gen_random_move_bot1(color, board)

        if best_move != None:
            self.make_move(color, board, best_move)
            
        return best_move
    
    def gen_move_bot2(self, color, board):
        estimation_available_moves = []
        for i in range(len(board.legal_moves)):
            estimation_available_moves.append(board.estimation[board.legal_moves[i]])
        moves_estimation_dict = dict(zip(board.legal_moves, estimation_available_moves))
        sorted_moves_estimation = sorted(moves_estimation_dict.items(), key=lambda item: item[1], reverse=True)
        # print(sorted_moves_estimation)
        if sorted_moves_estimation[0][1] >= 0:
            best_move = sorted_moves_estimation[0][0]
        else:
            best_move = None

        if best_move != None:
            self.make_move(color, board, best_move)
            
        return best_move
    
    def gen_move_bot3(self, color, board, game):
        best_move = self.minimax(board, 5, color, game, color, 4)[1] # depth and number of top moves

        if best_move != None:
            self.make_move(color, board, best_move)
            
        return best_move
        
    def minimax(self, position, depth, max_player, game, color, top_moves):
        best_move = None
        if depth == 0 or game.gamestate != 'active':
            # print ((game.score[color] + len(game.board.territory[color])) - (game.score[3-color] + len(game.board.territory[3-color])))
            return (game.score[color] + len(game.board.territory[color])) - (game.score[3-color] + len(game.board.territory[3-color])), best_move

        if max_player:
            maxEval = float('-inf')
            for move in game.board.take_top_estimation(top_moves):
            # for move in game.board.legal_moves:
                game_copy = game.simple_copy()
                position = game_copy.bot3_move(move)
                evaluation = self.minimax(position, depth-1, False, game_copy, color, top_moves)[0]
                if maxEval < evaluation:
                    best_move = move
                    maxEval = evaluation
            return maxEval, best_move
        else:
            minEval = float('+inf')
            for move in game.board.take_top_estimation(top_moves):
            # for move in game.board.legal_moves:
                game_copy = game.simple_copy()
                position = game_copy.bot3_move(move)
                evaluation = self.minimax(position, depth-1, True, game_copy, color, top_moves)[0]
                if minEval > evaluation:
                    best_move = move
                    minEval = evaluation
            return minEval, best_move