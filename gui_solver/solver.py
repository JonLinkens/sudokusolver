import math
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
import time
MARGIN = 5  # pixels around the board
SIDE = 50  # width of every board cell.
SLEEP = .1 # bigger value = slower visualisation


class SudokuSolve():

    def __init__(self, grid):
        self.grid = grid
        self.size = 9
    
    # str for debugging
    def __str__(self):
            st = ""
            for i in range(self.size):
                for j in range(self.size):
                    st += str(self.grid[i][j])+"  "
                st = st[:-2]
                st+="\n"
            return st

    # finding empty cells (value 0)
    # relpos stores coords in use
    def find_empty(self, relpos):
        for row in range(self.size):
            for col in range(self.size):
                if(self.grid[row][col] == 0):
                    relpos[0], relpos[1] = row, col
                    return False
        return True

    # checking validity of number in cell as per rules
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

    def solve(self, ui):
        relpos = [0,0]
        
        if self.find_empty(relpos):
            return True
        
        row = relpos[0]
        col = relpos[1]
        ui.insertNums(self.grid) # ui method call
        time.sleep(SLEEP)
        ui.canvas.update()
        
        for num in range(self.size+1):
            if self.isValid(row, col, num):
                self.grid[row][col] = num

                # success 
                if self.solve(ui):
                    return True
                #failure 
                self.grid[row][col] = 0
        return False




