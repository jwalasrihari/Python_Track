import numpy as np

class sudoko:
    grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]

    def possible(self,row, column, number):
        #Is the number appearing in the given row?
        for i in range(0,9):
            if self.grid[row][i] == number:
                return False

        #Is the number appearing in the given column?
        for i in range(0,9):
            if self.grid[i][column] == number:
                return False

        #Is the number appearing in the given square?
        x = (column // 3) * 3
        y = (row // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if self.grid[y+i][x+j] == number:
                    return False

        return True

    def solve(self):
        for row in range(0,9):
            for column in range(0,9):
                if self.grid[row][column] == 0:
                    for number in range(1,10):
                        if self.possible(row, column, number):
                            self.grid[row][column] = number
                            self.solve()
                            self.grid[row][column] = 0

                    return

        print(np.matrix(self.grid))
        input('More possible solutions')

obj=sudoko()
obj.solve()
