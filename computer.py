from bstree import BSTree
from copy import deepcopy


class Computer:
    def __init__(self, board):
        self.board = board
        self.tree = None

    def make_move(self):
        self.tree = BSTree(data=deepcopy(self.board))
        self.__fill_tree(self.tree)
        result1 = self.get_result(self.tree.left.get_leafs())
        result2 = self.get_result(self.tree.right.get_leafs())

        if result1 > result2:
            self.board.cells = self.tree.left.data.cells
        else:
            self.board.cells = self.tree.right.data.cells

        self.board.last_move = -self.board.last_move
        self.board.number_of_moves += 1

    def __fill_tree(self, tree):
        if tree.data.has_winner() == 0:
            moves = self.get_moves(tree.data)
            if moves:
                move1, move2 = moves
                board1 = deepcopy(tree.data)
                board2 = deepcopy(tree.data)

                board1.make_move(move1)
                board2.make_move(move2)

                tree.left = board1
                tree.right = board2

                self.__fill_tree(tree.right)
                self.__fill_tree(tree.left)

    @staticmethod
    def get_moves(board):
        possible_moves = board.get_possible_moves()
        if len(possible_moves) > 1:
            move2 = move1 = board.get_random_move()
            while move2 == move1:
                move2 = board.get_random_move()

            return move1, move2
        elif possible_moves == 1:
            return possible_moves[0], possible_moves[0]
        else:
            return None

    @staticmethod
    def get_result(leafs):
        result = 0

        for leaf in leafs:
            if leaf.data.has_winner() != 2:
                result += leaf.data.has_winner()

        return result
