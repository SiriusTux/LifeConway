+from board import Board

def main():
    user_rows = int(input('Insert number of rows: '))
    user_columns = int(input('Insert number of columns: '))
    game_board = Board(user_rows, user_columns)

    game_board.print_board()

    user_action = ''

    while user_action != 'q':

        user_action = input('Press any Enter to continue or q to quit: ')

        if user_action == '':
            game_board.update_board()
            game_board.print_board()


if __name__ == '__main__':

    print('#####################################')
    print('# Welcome to Life Conway simulation #')
    print('#####################################')

    main()
