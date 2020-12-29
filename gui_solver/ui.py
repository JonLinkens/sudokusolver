import time
from tkinter import Tk, Canvas, Frame, BOTH, TOP, BOTTOM

MARGIN = 5 
CELLWIDTH = 50  # size of each sudoku cell
WIDTH = HEIGHT = MARGIN * 2 + CELLWIDTH * 9 # width and height of the whole board


class SudokuUI(Frame):

    def __init__(self, parent, solver):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.resizable(False, False)
        self.row, self.col = -1, -1
        self.solver = solver
        self.initUI()
        self.drawGrid()
        self.insertNums(self.solver.grid)
        self.solver.solve(self)
        self.insertNums(self.solver.grid)
        
    # init window size etc
    def initUI(self):
        self.parent.title("Sudoku Solver")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(
            self, width=WIDTH, height=HEIGHT,
            highlightthickness=0
        )
        self.canvas.pack(fill=BOTH, side=TOP)
        

    # constructing grid lines
    def drawGrid(self):
        for i in range(10):
            self.canvas.create_line(
                MARGIN + i * CELLWIDTH, MARGIN,
                MARGIN + i * CELLWIDTH, HEIGHT - MARGIN,
                width=2, fill="black" if i % 3 == 0 else "gray"
            )
            self.canvas.create_line(
                MARGIN, MARGIN + i * CELLWIDTH,
                WIDTH - MARGIN, MARGIN + i * CELLWIDTH,
                width=2, fill="black" if i % 3 == 0 else "gray"
            )

    # inserting numbers into the sudoku
    def insertNums(self, grid):
        self.canvas.delete("numbers") # deleting existing to avoid multiple in same cell
        for i in range(9):
            for j in range(9):
                original = grid[i][j]
                if original != 0: # 0 = empty slot
                    self.canvas.create_text(
                        MARGIN + j * CELLWIDTH + CELLWIDTH / 2,
                        MARGIN + i * CELLWIDTH + CELLWIDTH / 2,
                        text=original, tags="numbers",
                        font=('Arial',20,'bold'), fill="black"
                    )