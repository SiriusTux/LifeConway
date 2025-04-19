from cell import Cell
from random import randint

class Board:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell(i, j) for j in range(self.columns)] for i in range(self.rows)]
        self.generate_board()

    def generate_board(self):
        # Ramndom init board status 66% chance cell is dead and 33% cell is alive
        for row in self.grid:
            for cell in row:
                random_number = randint(0,2)
                if random_number == 1:
                    cell.set_alive()

    def print_board(self):
        print('\n'*5)
        # Loop over rows and columns and print status characther on screen
        for row in self.grid:
            for cell in row:
                print(cell.get_print_char(), end='')
            print()

    def update_board(self):
        index = []
        # Loop over the rows and columns to find cells that change status
        # save position and new status of these cells in the list index
        for i in range(self.rows):
            for j in range(self.columns):
                cell = self.grid[i][j]
                new_cell_status = self.new_status(cell)
                if new_cell_status != cell.status:
                    index.append([cell, new_cell_status])
        # Update grid by looping over changed cells and change status
        for el in index:
            cell, new_status = el
            if new_status == 1:
                cell.set_alive()
            else:
                cell.set_dead() 
    
    def new_status(self, cell):
        nei_alive = self.check_nei(cell)
        # Game Life rules
        if cell.status == 1:
            # If cell is alive, cell dies if number of alive neighbours is less than 2 or greater than 3,
            # cell remains alive if number of alive neighbours is exactly 2 or 3
            if nei_alive < 2 or nei_alive > 3:
                return 0
            else:
                return 1
        else:
            # If cell is dead, cell reborns if it has exactly 3 neighbours
            # otherwise it remains dead
            if nei_alive == 3:
                return 1
            else:
                return 0
    
    def check_nei(self, cell):
        sum = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                a = (cell.x + i + self.rows) % self.rows
                b = (cell.y + j + self.columns) % self.columns
                sum += self.grid[a][b].status
        sum -= cell.status
        return sum


