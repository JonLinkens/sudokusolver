import math
class SudokuSolver():

    def __init__(self, size, grid):
        self.size = size
        self.grid = grid

    def __str__(self):
        st = ""
        for i in range(self.size):
            for j in range(self.size):
                st += str(self.grid[i][j])+"  "
            st = st[:-2]
            st+="\n"
        return st

    # finding empty cells (value 0)
    # relpos storing coords in use
    def find_empty(self, relpos):
        for row in range(self.size):
            for col in range(self.size):
                if(self.grid[row][col] == 0):
                    relpos[0], relpos[1] = row, col
                    return False
        return True

    # checking if the number is valid in row/column/subgrid
    def isValid(self, row, col, num):
        # row check
        for n in range(self.size):
            if(self.grid[row][n] == num):
                return False

        # col check
        for n in range(self.size):
            if(self.grid[n][col] == num):
                return False
        
        #subgrid check
        subsize = math.isqrt(self.size)
        srow = row - row % subsize
        scol = col - col % subsize
        for n in range(subsize):
            for j in range(subsize):
                if(self.grid[n + srow][j + scol] == num):
                    return False
        return True

    def solve(self):
        relpos = [0,0]

        if self.find_empty(relpos):
            return True
        
        row = relpos[0]
        col = relpos[1]

        # checking all nums for each cell
        for num in range(self.size+1):
            if self.isValid(row, col, num):
                self.grid[row][col] = num # temp num assignment

                # success check
                if self.solve():
                    return True

                #failure check
                self.grid[row][col] = 0
        return False

# -------------------------------------------

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

t = SudokuSolver(9,grid)

if t.solve():
    print(t)
else:
    print("No solution")


# Q 004300209005009001070060043006002087190007400050083000600000105003508690042910300
# A 864371259325849761971265843436192587198657432257483916689734125713528694542916378

# Q 040100050107003960520008000000000017000906800803050620090060543600080700250097100
# A 346179258187523964529648371965832417472916835813754629798261543631485792254397186