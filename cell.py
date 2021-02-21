
class Cell:

    # A cell is created with status = Dead
    def __init__(self):
        self.status = 'Dead'

    # Set cell status to dead
    def set_dead(self):
        self.status = 'Dead'

    # Set cell status to alive
    def set_alive(self):
        self.status = 'Alive'

    # Check if a cell is alive
    def is_alive(self):
        return self.status == 'Alive'

    # What the boart should print
    def get_print_char(self):
        if self.is_alive():
            return 'O'
        else:
            return ' '

