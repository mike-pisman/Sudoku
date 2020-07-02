import numpy as np
#import random
import time
import copy

class Sudoku:

    def __init__(self):
        self.board = self.generate_board()

    #Function generates board 9x9 with random numbers
    def generate_board(self):

        # List of 9 squares filled with zeroes
        square = np.zeros((9,3,3), int)
        #print(square)
        #for i in range(9):
            #square.append(np.zeros((3,3), int))

        # Fill each of 9 squares, left to right, top to bottom
        for i in range(4):
            for row in range(3):
                # Find all elements that are not present in the current row
                elements = [square[n][row] for n in range((i // 3)*3, i)]
                elements = np.setdiff1d(range(1,10), elements)

                # Find all elements that are not present in the current Square
                elements = np.setdiff1d(elements, square[i])

                # Choose elements so at least 3 elements are available for each row
                # These elements must be included in the current row
                test = set()
                for n in range(row, 2):
                    print(square[i-1][n+1])
                    test.update(square[i-1][n+1])
                #test = np.trim_zeros(np.intersect1d(elements, test, assume_unique=True))

                print(test)

                # If number of elements that have to be included is less than 3,
                # Chose random ones
                """if len(test) < 3:
                    elements = np.setdiff1d(elements, test)
                    elements = np.random.choice(elements, 3 - len(test), replace=False)

                    test = np.append(test, elements)
                """

                #Column
                square = self.transpose(square)

                for n in range(row, 2):
                    test.update(square[i-1][n+1])
                    #test = np.append(test, square[i-1][n+1]).astype(int)
                test = np.trim_zeros(np.intersect1d(elements, list(test), assume_unique=True))

                print(test)

                # If number of elements that have to be included is less than 3,
                # Chose random ones
                if len(test) < 3:
                    elements = np.setdiff1d(elements, test)
                    elements = np.random.choice(elements, 3 - len(test), replace=False)

                    test = np.append(test, elements)

                square = self.transpose(square)


                new_row = np.random.choice(test, 3, replace=False)

                square[i][row] = new_row

                self.print_board(square)

                #Column
                """
                new_row = np.zeros((3), int)

                for co in range(3):
                    col = []
                    for sq in range(i // 3):
                        icol = i - 3 * (sq + 1)
                        for rn in range(3):
                            col.append(square[icol][rn][co])

                    test = np.setdiff1d(elements, col)
                    print(test)
                    test = np.random.choice(test, 1, replace=False)
                    elements = elements[elements != test]
                    new_row[co] = test

                """

                #new_row = np.random.choice(elements, 3, replace=False)

                # Lastly, shuffle elements and fill the row



            """for i in range(3):
                for p in range(3):
                    print(square[i*3][p], square[i*3+1][p], square[i*3+2][p])
            print()
            """
        #print(square)

        # print(self.check(square))


        return square # return board

    # Function returns transposed board
    def transpose(self, board = None):
        if board is None:
            board = self.board

        new_board = np.empty((3,3), dtype=object)
        for j in range(3):
            for k in range(3):
                new_board[j, k] = np.transpose(board[j*3 + k])

        new_board = np.transpose(new_board)
        new_board = new_board.reshape((9))

        return new_board

    # Function returns True if each square and row has all 9 numbers
    def check(self, board):
        for i in range(3):
            if set(np.concatenate(board[i])) != set(range(1,10)):
               return False
            if set(np.concatenate((board[0][i], board[1][i], board[2][i]))) != set(range(1,10)):
                return False
            return True

    # Print the board
    def print_board(self, board = None):
        if board is None:
            board = self.board

        for i in range(3):
            for p in range(3):
                print(board[i*3][p], board[i*3+1][p], board[i*3+2][p])
            print()


def main():
    for _ in range(1):
        game = Sudoku()
        game.print_board()

if __name__ == "__main__":
    start = time.time()
    main()
    print('\n executed in', time.time() - start, 'second')

#game.print_board()
