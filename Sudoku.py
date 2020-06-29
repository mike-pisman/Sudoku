import numpy as np
#import random
import time

class Sudoku:

    def __init__(self):
        self.board = self.generate_board()

    #Function generates board 9x9 with random numbers
    def generate_board(self):

        square = []
        for i in range(9):
            square.append(np.zeros((3,3)))

        # Top left square
        square[0] = np.random.choice(range(1,10), 9, replace=False)
        square[0] = square[0].reshape(3,3)

        # Top middle square
        square[1] = np.zeros((3,3), dtype=int)

        elements = np.setdiff1d(range(1,10), square[0][0])
        square[1][0] = np.random.choice(elements, 3, replace=False)

        elements = np.setdiff1d(range(1,10), square[0][1])
        elements = np.setdiff1d(elements, square[1])
        test = np.intersect1d(elements, square[0][2], assume_unique=True)

        if len(test) < 3:
            elements = np.setdiff1d(elements, test)
            elements = np.random.choice(elements, 3 - len(test), replace=False)
            test = np.append(test, elements)

        square[1][1] = test

        elements = np.setdiff1d(range(1,10), square[1])
        square[1][2] = np.random.choice(elements, 3, replace=False)

        # Top right square
        square[2] = np.zeros((3,3), dtype=int)
        for i in range(3):
            elements = np.setdiff1d(range(1,10), np.append(square[0][i], square[1][i]))
            square[2][i] = np.random.choice(elements, 3, replace=False)

        # Middle left square
        square[3] = np.zeros((3,3), dtype=int)
        for i in range(3):
            elements = np.setdiff1d(range(1,10), np.append(square[0][i], square[1][i]))
            square[2][i] = np.random.choice(elements, 3, replace=False)

        for i in range(3):
            print(square[0][i], square[1][i], square[2][i])

    def print_board(self):
        print( *(self.board), sep = "\n" )

def main():
    cleargame = Sudoku()


if __name__ == "__main__":
    start = time.time()
    main()
    print('\n executed in', time.time() - start, 'second')

#game.print_board()
