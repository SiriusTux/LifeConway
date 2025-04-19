class Cell:

    # A cell i create in position (x, y)
    # A cell is created with status = Dead (0)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = 0

    # Set cell status to dead
    def set_dead(self):
        self.status = 0

    # Set cell status to alive
    def set_alive(self):
        self.status = 1

    # Check if a cell is alive
    def is_alive(self):
        return self.status == 1

    # What the boart should print
    def get_print_char(self):
        if self.is_alive():
            return 'O'
        else:
            return ' '



