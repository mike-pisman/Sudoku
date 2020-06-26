import numpy as np
import random

class Sudoku:

    def __init__(self):
        self.board = self.generate_board()

    #Function generates board 9x9 with random numbers
    def generate_board(self):

        first_sq = np.array(np.random.choice(range(1, 10), 9, replace=False))
        first_sq = first_sq.reshape(3,3)

        second_sq = []

        for i in range(3):
            elements = np.setdiff1d(range(1, 10), first_sq[i])
            row = np.random.choice(elements, 3, replace=False)
            second_sq = np.append(second_sq, row, axis=0)

        print(first_sq.astype(int).reshape((3,3)))
        print(second_sq.astype(int).reshape((3,3)))




        #board = np.array(([square.reshape(3,3) for i in range(9)]))
        #print(board)


        """row = []
        row[0] = firstRow = random.sample(range(1,10), 9)
        permutes = random.sample(range(1,10),9)

        for i in permutes:
            while(sum(row[i // 3] + row[i:i+3] // 3)
                return list(firstRow[i:]+firstRow[:i] )
        """

    def print_board(self):
        print( *(self.board), sep = "\n" )

game = Sudoku()
#game.print_board()
