def is_sunk(ship):
    """
    A ship is sunk if the number of successful hits (len(ship[4])) is equal to the length (ship[3]) of the ship.
    :param ship: tuple.
    :return: Boolean value; True if ship is sunk, otherwise False.
    """

    if ship[3] == len(ship[4]):
        return True
    else:
        return False


def ship_type(ship):
    """
    Depending on length of ship (ship[3]) return name of ship.
    :param ship: tuple.
    :return: string with the name of the ship.
    """

    if ship[3] == 1:
        return 'submarine'
    elif ship[3] == 2:
        return 'destroyer'
    elif ship[3] == 3:
        return 'cruiser'
    elif ship[3] == 4:
        return 'battleship'
    else:
        return 'A ship\'s length is from 1 to 4'


def fleet_squares(fleet):
    """
    The list produced will be used in functions is_open_sea and check_if_hits below.
    :param fleet: list of tuples.
    :return: a list which contains all squares that contain a ship.
    """

    fleet_coord = []
    for ship in fleet:
        list_ship = list(ship)
        if list_ship[2]:  # check direction of ship is horizontal
            i = list_ship[1]
            for col in range(list_ship[3]):
                square = (list_ship[0], i)
                fleet_coord.append(square)
                i += 1

        elif not list_ship[2]:  # check direction of ship is vertical
            i = list_ship[0]
            for rows in range(list_ship[3]):
                square = (i, list_ship[1])
                fleet_coord.append(square)
                i += 1

    return fleet_coord


def is_open_sea(row, column, fleet):
    """
    Iterate through fleet using function fleet_coord. Create a list open_sea_squares that contains all squares
    adjacent to (row, column).
    :param row: int; range (0, 9)
    :param column: int; range (0, 9)
    :param fleet: list of tuples
    :return: Boolean value. True if all squares adjacent to given (row, column) are empty. Otherwise, return False.
    """

    open_sea_squares = []
    for rows in range(-1, 2):
        row_open_sea = row + rows
        if row_open_sea < 0 or row_open_sea > 9:  # if row is outside the board, then skip iteration
            continue
        for columns in range(-1, 2):
            col_open_sea = column + columns
            if col_open_sea < 0 or col_open_sea > 9:  # if column is outside the board, then skip iteration
                continue
            square = (row_open_sea, col_open_sea)
            open_sea_squares.append(square)

    for square in open_sea_squares:
        if square in fleet_squares(fleet):
            return False
    return True


def ok_to_place_ship_at(row, column, horizontal, length, fleet):
    """
    Using function open_sea for each square of ship, we check if all squares adjacent to that is empty. If this is True
    for all squares of ship, then the ship can be placed.
    :param row: int; range (0, 9).
    :param column: int; range (0, 9).
    :param horizontal: Boolean value; True if horizontal, otherwise False.
    :param length: int; range (1, 4).
    :param fleet: list of tuples.
    :return: Boolean value; True if given ship can be placed on board, otherwise False.
    """

    ship_squares = []
    if horizontal:  # check direction of ship
        counter = column
        for col in range(length):
            if counter > 9:  # if row is outside the board, return False (illegal placement)
                return False
            square = (row, counter)
            ship_squares.append(square)
            counter += 1

    elif not horizontal:  # check direction of ship is vertical
        counter = row
        for rows in range(length):
            if counter > 9:  # if column is outside the board, return False (illegal placement)
                return False
            square = (counter, column)
            ship_squares.append(square)
            counter += 1

    for square in ship_squares:
        if not is_open_sea(square[0], square[1], fleet):
            return False
    return True


def place_ship_at(row, column, horizontal, length, fleet):
    """
    We append each ship to fleet and, eventually, add this to board.
    :param row: int; range (0, 9).
    :param column: int; range (0, 9).
    :param horizontal: Boolean value; True if horizontal, otherwise False.
    :param length: int; range (1, 4).
    :param fleet: list of tuples.
    :return: updated fleet with ships that are ok to place.
    """
    new_ship = (row, column, horizontal, length, set())
    fleet.append(new_ship)
    return fleet


def randomly_place_all_ships():
    """
    For this function, import the random library. Then append a ship to the list fleet, starting from the
    battleship (one ship of 4 sq), then cruisers (two ships of 3 sq), destroyers (three ships of 2sq) and lastly
    submarines (four ships of 1 sq). row, column and direction of each ship are selected in random. Depending on the
    size of each ship, we check direction of ship and if ship placement would be out of board (for example a battleship
    can be placed on (9, 0) horizontally, but not vertically). We use a counter for each ship type to avoid having a
    fleet with less than 10 ships in case not ok_to_place_ship_at.
    """
    import random

    fleet = []

    counter = 0
    while counter < 1:
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        direction = [True, False]
        horizontal = random.choice(direction)
        if ok_to_place_ship_at(row, column, horizontal, 4, fleet):
            if row <= 6 and column <= 6:
                place_ship_at(row, column, horizontal, 4, fleet)
                counter += 1
            elif row > 6 and column <= 6 and horizontal:
                place_ship_at(row, column, horizontal, 4, fleet)
                counter += 1
            elif column > 6 and row <= 6 and not horizontal:
                place_ship_at(row, column, horizontal, 4, fleet)
                counter += 1
            else:
                counter += 0

    counter = 0
    while counter < 2:
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        direction = [True, False]
        horizontal = random.choice(direction)
        if ok_to_place_ship_at(row, column, horizontal, 3, fleet):
            if row <= 7 and column <= 7:
                place_ship_at(row, column, horizontal, 3, fleet)
                counter += 1
            elif row > 7 and column <= 7 and horizontal:
                place_ship_at(row, column, horizontal, 3, fleet)
                counter += 1
            elif column > 7 and row <= 7 and not horizontal:
                place_ship_at(row, column, horizontal, 3, fleet)
                counter += 1
            else:
                counter += 0

    counter = 0
    while counter < 3:
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        direction = [True, False]
        horizontal = random.choice(direction)
        if ok_to_place_ship_at(row, column, horizontal, 2, fleet):
            if row <= 8 and column <= 8:
                place_ship_at(row, column, horizontal, 2, fleet)
                counter += 1
            elif row > 8 and column <= 8 and horizontal:
                place_ship_at(row, column, horizontal, 2, fleet)
                counter += 1
            elif column > 8 and row <= 8 and not horizontal:
                place_ship_at(row, column, horizontal, 2, fleet)
                counter += 1
            else:
                counter += 0

    counter = 0
    while counter < 4:
        row = random.randint(0, 9)
        column = random.randint(0, 9)
        if ok_to_place_ship_at(row, column, True, 1, fleet):
            place_ship_at(row, column, True, 1, fleet)
            counter += 1
        else:
            counter += 0

    return fleet


def check_if_hits(row, column, fleet):
    """
    Check if (row, column) is included in any of the squares occupied by a ship (using function fleet_squares to create
    list that contains all squares occupied by a ship).
    :param row: int; range (0, 9).
    :param column: int; range (0, 9).
    :param fleet: list of tuples.
    :return: Boolean value. True if (row, column) leads to successful hit in fleet.
    """

    hit_coord = (row, column)

    return hit_coord in fleet_squares(fleet)


def hit(row, column, fleet):
    """
    Assume that every hit results in a successful hit. Iterate through fleet to find the ship that has received the hit.
    Add hit to ship's set of hits.
    :param row: int; range (0, 9).
    :param column: int; range (0, 9).
    :param fleet: list of tuples.
    :return: a tuple that contains the updated fleet and the ship that has received the hit.
    """

    hit_coord = (row, column)
    hit_ship = None

    for ship in fleet:
        ship_coord = []
        list_ship = list(ship)
        if list_ship[2]:  # check direction of ship is horizontal
            i = list_ship[1]
            for col in range(list_ship[3]):
                square = (list_ship[0], i)
                ship_coord.append(square)
                i += 1

            if hit_coord in ship_coord:
                ship[4].add(hit_coord)
                hit_ship = ship
            else:
                continue

        elif not list_ship[2]:  # check direction of ship is vertical
            i = list_ship[0]
            for rows in range(list_ship[3]):
                square = (i, list_ship[1])
                ship_coord.append(square)
                i += 1

            if hit_coord in ship_coord:
                ship[4].add(hit_coord)
                hit_ship = ship
            else:
                continue

    return fleet, hit_ship


def are_unsunk_ships_left(fleet):
    """
    Using function is_sunk, we iterate through the fleet and check if there are unsunk ships left.
    :param fleet: list of tuples.
    :return: Boolean value. True if not all ships are sunk, otherwise False.
    """

    sunk_ships = 0
    for ship in fleet:
        if is_sunk(ship):
            sunk_ships += 1

    if sunk_ships == 10:
        return False
    else:
        return True


def main():
    current_fleet = randomly_place_all_ships()
    game_over = False
    shots = 0

    hits = []  # a list to store all successful hits

    while not game_over:
        try:
            loc_str = input('Enter row and column to shoot (separated by space) or enter "quit" to end game: ')
            if loc_str == 'quit':  # user input to end game at any time
                exit('Game ended successfully.')

            loc_lst = loc_str.split(' ')
            current_row = int(loc_lst[0])
            current_column = int(loc_lst[1])

            if current_row > 9 or current_row < 0 or current_column > 9 or current_column < 0:
                raise ValueError

            shots += 1

            if (current_row, current_column) in hits:  # we check if user tries to hit a square that already has been
                print('You missed!')  # hit before

            elif check_if_hits(current_row, current_column, current_fleet):
                print('You have a hit!')
                (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
                hit_coord = (current_row, current_column)
                hits.append(hit_coord)
                if is_sunk(ship_hit):
                    print('You sank a ' + ship_type(ship_hit) + '!')
            else:
                print('You missed!')

            if not are_unsunk_ships_left(current_fleet):
                game_over = True

        except ValueError:
            print('You need to enter two integer numbers (from 0 to 9) separated by space.')
            continue
        except IndexError:
            print('You need to enter two integer numbers (from 0 to 9) separated by space.')
            continue

    print('Game over! You required', shots, 'shots.')


if __name__ == '__main__':  # keep this in
    main()
