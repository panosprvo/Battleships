"""
For the visualization of battleships.py, we import battleships to this file. We create a board that represents the sea.
At first the whole board is unknown and gradually, with user input, we try to sink the fleet in as less hits as
possible. With each hit the board is printed with the current hit outcome. A '.' represents unknown waters, a 'M'
represents a miss and a 'H' represents a successful hit. When a ship is successfully sunk, hits on board for
for specific ship, change to the type of ship (B for battleship, C for cruiser, D for destroyer and S for submarine).
"""
from battleships import *

print('Welcome to \033[1mBattleships!\033[0m',
      'The purpose of the game is to sink the enemy fleet, which consists of 10 ships.',
      'One battleship, two cruisers, three destroyers and four submarines.',
      'To initiate an attack, enter two coordinates each one ranging from 0 to 9.', sep='\n')
print()

board = [
        ['   ', ' 0 ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 '],
        ['  ------------------------------'],
        ['0 ', '|', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
        ['1 ', '|', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
        ['2 ', '|', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
        ['3 ', '|', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
        ['4 ', '|', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
        ['5 ', '|', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
        ['6 ', '|', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
        ['7 ', '|', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
        ['8 ', '|', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . '],
        ['9 ', '|', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ', ' . ']
        ]

current_fleet = randomly_place_all_ships()

# Create a list that will contain lists of tuples, each one containing all the squares each ship occupies. When a ship
# is sunk we iterate through ship_squares to find the ship that was sunk and change the values on the printed board,
# depending on type of ship.

ship_squares = []
ship_counter = 0
for ship in current_fleet:
    list_ship = list(ship)

    if list_ship[2]:  # check direction of ship is horizontal
        i = list_ship[1]
        ship_squares.append([])
        for col in range(list_ship[3]):
            square = (list_ship[0], i)
            ship_squares[ship_counter].append(square)
            i += 1
        ship_counter += 1

    elif not list_ship[2]:  # check direction of ship is vertical
        i = list_ship[0]
        ship_squares.append([])
        for rows in range(list_ship[3]):
            square = (i, list_ship[1])
            ship_squares[ship_counter].append(square)
            i += 1
        ship_counter += 1

game_over = False
shots = 0
ships_left = 10
hits = []

while not game_over:
    try:
        loc_str = input('Enter row and column to shoot (separated by space) or enter "quit" to end game: ')

        if loc_str == 'quit':
            exit('Game ended successfully.')

        loc_lst = loc_str.split(' ')
        current_row = int(loc_lst[0])
        current_column = int(loc_lst[1])

        if current_row > 9 or current_row < 0 or current_column > 9 or current_column < 0:
            raise ValueError

        shots += 1

        if (current_row, current_column) in hits:
            print('You missed!')
            for square in board:
                print(''.join(square))

        elif check_if_hits(current_row, current_column, current_fleet):
            print('You have a hit!')
            board[current_row + 2][current_column + 2] = '\033[1m H \033[0m'  #add 2 to avoid top and side numbers of
                                                                              # the board

            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            hit_coord = (current_row, current_column)
            hits.append(hit_coord)
            if is_sunk(ship_hit):
                ships_left -= 1
                print('You sank a ' + ship_type(ship_hit) + '!')
                print('There are ' + str(ships_left) + ' ships left to sink!')
                ship_index = current_fleet.index(ship_hit)
                for index in (ship_squares[ship_index]):
                    (row, column) = index
                    if len(ship_squares[ship_index]) == 4:  #if the size of the list is 4, then it is a battleship
                        board[row+2][column+2] = '\033[1m B \033[0m'
                    elif len(ship_squares[ship_index]) == 3:  #if the size of the list is 3, then it is a cruiser
                        board[row+2][column+2] = '\033[1m C \033[0m'
                    elif len(ship_squares[ship_index]) == 2:  #if the size of the list is 2, then it is a destroyer
                        board[row+2][column+2] = '\033[1m D \033[0m'
                    else:  #the size of the list in 1, and the ship that was sunk was s submarine
                        board[row+2][column+2] = '\033[1m S \033[0m'

                for square in board:
                    print(''.join(square))
            else:
                for square in board:
                    print(''.join(square))
        else:
            print('You missed!')
            board[current_row + 2][current_column + 2] = ' M '  #add 2 to avoid top and side numbers of the board
            for square in board:
                print(''.join(square))

        if not are_unsunk_ships_left(current_fleet):
            game_over = True

    except ValueError:
        print('You need to enter two integer numbers (from 0 to 9) separated by space.')
        continue
    except IndexError:
        print('You need to enter two integer numbers (from 0 to 9) separated by space.')
        continue

print('Game over! You required', shots, 'shots.')
