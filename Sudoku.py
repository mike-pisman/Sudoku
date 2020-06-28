import numpy as np
#import random
import time

class Sudoku:

    def __init__(self):
        self.board = self.generate_board()

    #Function generates board 9x9 with random numbers
    def generate_board(self):

        # Top left square
        first_sq = np.random.choice(range(1,10), 9, replace=False)
        first_sq = first_sq.reshape(3,3)

        # Top middle square
        second_sq = np.zeros((3,3), dtype=int)

        elements = np.setdiff1d(range(1,10), first_sq[0])
        second_sq[0] = np.random.choice(elements, 3, replace=False)

        elements = np.setdiff1d(range(1,10), first_sq[1])
        elements = np.setdiff1d(elements, second_sq)
        test = np.intersect1d(elements, first_sq[2], assume_unique=True)

        if len(test) < 3:
            elements = np.setdiff1d(elements, test)
            elements = np.random.choice(elements, 3 - len(test), replace=False)
            test = np.append(test, elements)

        second_sq[1] = test

        elements = np.setdiff1d(range(1,10), second_sq)
        second_sq[2] = np.random.choice(elements, 3, replace=False)

        # Top middle square
        third_sq = np.zeros((3,3), dtype=int)
        for i in range(3):
            elements = np.setdiff1d(range(1,10), np.append(first_sq[i], second_sq[i]))
            third_sq[i] = np.random.choice(elements, 3, replace=False)


        for i in range(3):
            print(first_sq[i], second_sq[i], third_sq[i])

    def print_board(self):
        print( *(self.board), sep = "\n" )

def main():
    start = time.time()
    game = Sudoku()
    print('\n executed in', time.time() - start, 'second')

if __name__ == "__main__":
    main()

#game.print_board()
