from cell import Cell
from random import randint

class Board:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell() for j in range(self.columns)] for i in range(self.rows)]
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
                cell_status = self.grid[i][j].status
                new_cell_status = self.check_nei(i, j)
                if new_cell_status != cell_status:
                    index.append((i,j, new_cell_status))
        # Update grid by looping over changed cells and change status
        for el in index:
            cell = self.grid[el[0]][el[1]]
            if el[2] == 'Alive':
                cell.set_alive()
            else:
                cell.set_dead() 

    
    def check_nei(self, row, col):
        cell = self.grid[row][col]
        # Get neighbour's group and count alive neighbours
        cell_nei = self.get_nei(row, col)
        nei_alive = self.count_alive(cell_nei)
        # Game Life rules
        if cell.is_alive():
            # If cell is alive, cell dies if number of alive neighbours is less than 2 or greater than 3,
            # cell remains alive if number of alive neighbours is exactly 2 or 3
            if nei_alive < 2 or nei_alive > 3:
                return 'Dead'
            else:
                return 'Alive'
        else:
            # If cell is dead, cell reborns if it has exactly 3 neighbours
            # otherwise it remains dead
            if nei_alive == 3:
                return 'Alive'
            else:
                return 'Dead'

    def count_alive(self, group):
        # Count number of alive neighbours
        count = 0
        for cell in group:
            if cell.is_alive():
                count += 1
        return count

    def get_nei(self, row, col):
        up, down, right, left = self.get_step(row, col)
        # Take all neighbours in generic case
        nei =   [ 
                    self.grid[row-up][col-left], self.grid[row-up][col], self.grid[row-up][col+right],
                    self.grid[row][col-left], self.grid[row][col], self.grid[row][col+right],
                    self.grid[row+down][col-left], self.grid[row+down][col], self.grid[row+down][col+right]
        ]
        # Remove duplicated neighbours, due to steps combination (es. if up=0 self.grid[row-up][col]=self.grid[row][col])
        nei = list(set(nei))
        # Remove central cell
        nei.remove(self.grid[row][col])
        return nei

    def get_step(self, row, col):
        # Start with all zero step
        up_step, down_step, right_step, left_step = 0, 0, 0, 0
        # If first row, no up step 
        if row > 0:
            up_step = 1
        # If last row you, no down step
        if row < self.rows - 1:
            down_step = 1
        # If first column, no left step
        if col > 0:
            left_step = 1
        # If last column, no right step
        if col < self.columns - 1:
            right_step = 1
        return up_step, down_step, right_step, left_step 



