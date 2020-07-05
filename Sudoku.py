import numpy as np
#import random
import time

class Sudoku:

    def __init__(self):
        self.board = self.generate_board()

    #Function generates board 9x9 with random numbers
    def generate_board(self):

        board = np.empty((3,3), dtype=object)
        for j in range(3):
            for k in range(3):
                board[j][k] = np.zeros((3,3), int)

        for j in range(3):
            for k in range(3):
                square = board[j][k]
                availeble_elements = range(1,10)

                for square_row in range(3):

                    # remove all from the same row
                    row_elements = []
                    for i in range(k):
                        row_elements.append(board[j][i][square_row])

                    row_elements = np.setdiff1d(availeble_elements, row_elements)

                    if len(row_elements) > 3:
                        if square_row == 1 and k > 0:
                            intersect = []

                            for i in range(k):
                                intersect = np.append(intersect, board[j][i][2])

                            intersect = np.trim_zeros(np.intersect1d(row_elements, intersect, assume_unique=True))

                            if len(intersect) < 3:
                                temp = np.setdiff1d(row_elements, intersect)
                                temp = np.random.choice(temp, 3 - len(intersect), replace=False)
                                row_elements = np.append(intersect, temp)
                            else:
                                row_elements = intersect


                    for square_col in range(3):
                        new_number = np.random.choice(row_elements, 1, replace=False)[0]
                        square[square_row][square_col] = new_number
                        row_elements = np.delete(row_elements, np.where(row_elements == new_number))

                        #self.print_board(board)

                    availeble_elements = np.setdiff1d(availeble_elements, square[square_row])


        return board # return board

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
    def check(self, board = None):
        if board is None:
            board = self.board

        for j in range(3):
            for k in range(3):
                if set(np.concatenate(board[j][k])) != set(range(1,10)):
                   return False
                if set(np.concatenate((board[j][0][k], board[j][1][k], board[j][2][k]))) != set(range(1,10)):
                   return False
            return True

    # Print the board
    def print_board(self, board = None):
        if board is None:
            board = self.board

        print()
        for j in range(3):
            for row in range(3):
                for k in range(3):
                    print(' ', end='')
                    for col in range(3):
                        print(board[j][k][row][col], end=' ')
                    print(' ', end='')
                print()
            print()

def main():
    for _ in range(1000):
        game = Sudoku()
        #game.print_board()
        print(game.check())

if __name__ == "__main__":
    start = time.time()
    main()
    print('\n executed in', time.time() - start, 'second')
