'''
PROGRAM DESCRIPITON:
	With using Python Numpy module create a game of SUDOKU.
    Please consider the following points while creating your project :-
        1) Use only the Numpy module not anything else of Python Data Science.
        2) Write your program using the OOPS concept of Python.
'''

# PROGRAMMED BY : Badam Jwala Sri Hari
# MAIL ID       : jwalasrihari1330@gmail.com
# DATE          : 03-09-2021
# PYTHON VERSION: 3.9.7
# NUMPY VERSION : 1.21.2
# CAVEATS       : None
# LICENSE       : None


import numpy as np

class sudoku:

    # Sudoku to be solved
    grid = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,0,1,9,0,0,5],
            [0,0,0,0,0,0,0,0,0]]

    # Checks whether a number can be place in a postion or not
    def possible(self,row, column, number):
        # Is the number appearing in the given row?
        for i in range(0,9):
            if self.grid[row][i] == number:
                return False

        # Is the number appearing in the given column?
        for i in range(0,9):
            if self.grid[i][column] == number:
                return False

        # Is the number appearing in the given square?
        x = (column // 3) * 3
        y = (row // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if self.grid[y+i][x+j] == number:
                    return False

        return True

    def solve(self):
        # Iterates over a grid(sudoku)
        for row in range(0,9):
            for column in range(0,9):
                if self.grid[row][column] == 0:
                    # Checking every possible number in postion
                    for number in range(1,10):
                        if self.possible(row, column, number):
                            self.grid[row][column] = number
                            self.solve()
                            # If we are strucked a some point we will backtrack and place Zero
                            self.grid[row][column] = 0
                    return
        print(np.matrix(self.grid))
obj=sudoku()
obj.solve()




'''
output:

[[5 3 4 6 7 8 1 9 2]
 [6 7 2 1 9 5 3 4 8]
 [1 9 8 3 4 2 5 6 7]
 [8 5 9 7 6 1 4 2 3]
 [4 2 6 8 5 3 9 7 1]
 [7 1 3 9 2 4 8 5 6]
 [9 6 1 5 3 7 2 8 4]
 [2 8 7 4 1 9 6 3 5]
 [3 4 5 2 8 6 7 1 9]]
 '''
