from tkinter import Tk
from solver import SudokuSolve
from ui import SudokuUI

level_name = "two" # name of .sudoku file to solve 
                       # structured as 9 lines of 9 integers 

# File Parsing ------------------------------------------
with open('%s.sudoku' % level_name, 'r') as file:
    grid = [[0 for x in range(9)] for x in range(9)]
    data = file.read().splitlines()
    for line, yval in enumerate(data):
        for char, xval in enumerate(yval):
            grid[line][char] = int(xval)
# -------------------------------------------------------

root = Tk() # root window
solve = SudokuSolve(grid) 
ui = SudokuUI(root, solve)
root.mainloop() # so window does not close upon solving