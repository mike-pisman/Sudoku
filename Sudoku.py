import numpy as np
import random

class Sudoku:

    def __init__(self):
        self.board = self.generate_board()

    #Function generates board 9x9 with random numbers
    def generate_board(self):
        firstRow = random.sample(range(1,10),9)
        permutes = random.sample(range(1,10),9)
        return list(firstRow[i:]+firstRow[:i] for i in permutes)

    def print_board(self):
        print( *(self.board), sep = "\n" )

game = Sudoku()
game.print_board()
