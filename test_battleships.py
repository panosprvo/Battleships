from battleships import *


def test_is_sunk1():
    s = (2, 3, False, 1, {(2, 3)})
    assert is_sunk(s) == True


def test_is_sunk2():
    s = (2, 3, False, 2, {(2, 3), (3, 3)})
    assert is_sunk(s) == True


def test_is_sunk3():
    s = (2, 3, False, 3, {(2, 3), (3, 3), (4, 3)})
    assert is_sunk(s) == True


def test_is_sunk4():
    s = (2, 3, False, 4, {(2, 3), (3, 3), (4, 3), (5, 3)})
    assert is_sunk(s) == True


def test_is_sunk5():
    s = (2, 3, False, 1, set())
    assert is_sunk(s) == False


def test_is_sunk6():
    s = (2, 3, False, 2, {(3, 3)})
    assert is_sunk(s) == False


def test_is_sunk7():
    s = (2, 3, False, 3, {(3, 3), (4, 3)})
    assert is_sunk(s) == False


def test_is_sunk8():
    s = (2, 3, False, 4, {(2, 3), (3, 3), (5, 3)})
    assert is_sunk(s) == False


def test_ship_type1():
    s = (4, 4, False, 3, set())
    assert ship_type(s) == 'cruiser'


def test_ship_type2():
    s = (5, 2, False, 2, set())
    assert ship_type(s) == 'destroyer'


def test_ship_type3():
    s = (6, 6, False, 1, set())
    assert ship_type(s) == 'submarine'


def test_ship_type4():
    s = (0, 3, False, 4, set())
    assert ship_type(s) == 'battleship'


def test_ship_type5():
    s = (4, 4, False, 6, set())
    assert ship_type(s) == 'A ship\'s length is from 1 to 4'


def test_fleet_squares1():
    f_fs = []
    expected = []
    assert fleet_squares(f_fs) == expected


def test_fleet_squares2():
    f_fs = [(2, 1, False, 3, set()), (0, 3, True, 1, set())]
    expected = [(2, 1), (3, 1), (4, 1), (0, 3)]
    assert fleet_squares(f_fs) == expected


def test_fleet_squares3():
    f_fs = [(2, 1, False, 3, set()), (0, 4, True, 1, set()), (8, 1, True, 3, set())]
    expected = [(2, 1), (3, 1), (4, 1), (0, 4), (8, 1), (8, 2), (8, 3)]
    assert fleet_squares(f_fs) == expected


def test_fleet_squares4():
    f_fs = [(2, 1, False, 3, set()), (0, 4, True, 1, set()), (8, 1, True, 3, set()), (7, 5, True, 2, set()),
            (3, 9, False, 2, set())]
    expected = [(2, 1), (3, 1), (4, 1), (0, 4), (8, 1), (8, 2), (8, 3), (7, 5), (7, 6), (3, 9), (4, 9)]
    assert fleet_squares(f_fs) == expected


def test_fleet_squares5():
    f_fs = [(3, 3, False, 4, set()), (8, 1, True, 3, set()), (2, 1, False, 3, set()), (3, 9, False, 2, set()),
            (1, 7, True, 2, set()), (7, 5, True, 2, set()), (9, 9, True, 1, set()), (6, 9, True, 1, set()),
            (0, 3, True, 1, set()), (0, 0, True, 1, set())]
    expected = [(3, 3), (4, 3), (5, 3), (6, 3), (8, 1), (8, 2), (8, 3), (2, 1), (3, 1), (4, 1), (3, 9), (4, 9), (1, 7),
                (1, 8), (7, 5), (7, 6), (9, 9), (6, 9), (0, 3), (0, 0)]
    assert fleet_squares(f_fs) == expected


s1 = (2, 8, False, 3, set())
s2 = (3, 4, True, 2, set())
f = [s1, s2]


def test_is_open_sea1():
    assert is_open_sea(6, 7, f) == True


def test_is_open_sea2():
    assert is_open_sea(2, 8, f) == False


def test_is_open_sea3():
    assert is_open_sea(2, 7, f) == False


def test_is_open_sea4():
    assert is_open_sea(2, 6, f) == False


def test_is_open_sea5():
    assert is_open_sea(0, 0, f) == True


def test_is_open_sea6():
    assert is_open_sea(9, 0, f) == True


def test_is_open_sea7():
    assert is_open_sea(0, 9, f) == True


def test_is_open_sea8():
    assert is_open_sea(9, 9, f) == True


empty_fleet = []


def test_is_open_sea9():
    assert is_open_sea(6, 7, empty_fleet) == True


def test_ok_to_place_ship_at1():
    assert ok_to_place_ship_at(5, 3, True, 2, f) == True


def test_ok_to_place_ship_at2():
    assert ok_to_place_ship_at(2, 4, True, 3, f) == False


def test_ok_to_place_ship_at3():
    assert ok_to_place_ship_at(1, 9, True, 1, f) == False


def test_ok_to_place_ship_at4():
    assert ok_to_place_ship_at(3, 0, True, 3, f) == True


def test_ok_to_place_ship_at5():
    assert ok_to_place_ship_at(4, 8, True, 2, f) == False


def test_ok_to_place_ship_at6():
    assert ok_to_place_ship_at(9, 0, True, 4, f) == True


def test_ok_to_place_ship_at7():
    assert ok_to_place_ship_at(9, 0, False, 3, f) == False


def test_ok_to_place_ship_at8():
    assert ok_to_place_ship_at(9, 9, True, 2, f) == False


def test_ok_to_place_ship_at9():
    assert ok_to_place_ship_at(9, 9, False, 2, f) == False


def test_ok_to_place_ship_at10():
    assert ok_to_place_ship_at(0, 9, False, 4, f) == False


def test_ok_to_place_ship_at11():
    assert ok_to_place_ship_at(0, 9, False, 2, f) == False


def test_ok_to_place_ship_at12():
    assert ok_to_place_ship_at(0, 9, True, 1, f) == True


def test_ok_to_place_ship_at13():
    assert ok_to_place_ship_at(9, 9, True, 1, f) == True


def test_ok_to_place_ship_at14():
    assert ok_to_place_ship_at(9, 0, True, 1, f) == True


def test_place_ship_at1():
    actual = place_ship_at(4, 2, False, 4, f)
    actual.sort()
    expected = [s1, s2, (4, 2, False, 4, set())]
    expected.sort()
    assert actual == expected


s3 = (4, 2, False, 4, set())


def test_place_ship_at2():
    actual = place_ship_at(8, 4, True, 1, f)
    actual.sort()
    expected = [s1, s2, s3, (8, 4, True, 1, set())]
    expected.sort()
    assert actual == expected


s4 = (8, 4, True, 1, set())


def test_place_ship_at3():
    actual = place_ship_at(8, 7, True, 1, f)
    actual.sort()
    expected = [s1, s2, s3, s4, (8, 7, True, 1, set())]
    expected.sort()
    assert actual == expected


s5 = (8, 7, True, 1, set())


def test_place_ship_at4():
    actual = place_ship_at(0, 5, True, 1, f)
    actual.sort()
    expected = [s1, s2, s3, s4, s5, (0, 5, True, 1, set())]
    expected.sort()
    assert actual == expected


s6 = (0, 5, True, 1, set())


def test_place_ship_at5():
    actual = place_ship_at(1, 1, True, 2, f)
    actual.sort()
    expected = [s1, s2, s3, s4, s5, s6, (1, 1, True, 2, set())]
    expected.sort()
    assert actual == expected


f1 = [(3, 3, False, 4, set()), (8, 1, True, 3, set()), (2, 1, False, 3, set()), (3, 9, False, 2, set()),
      (1, 7, True, 2, set()), (7, 5, True, 2, set()), (9, 9, True, 1, set()), (6, 9, True, 1, set()),
      (0, 3, True, 1, set()), (0, 0, True, 1, set())]


def test_check_if_hits1():
    assert check_if_hits(2, 1, f1) == True


def test_check_if_hits2():
    assert check_if_hits(5, 3, f1) == True


def test_check_if_hits3():
    assert check_if_hits(7, 6, f1) == True


def test_check_if_hits4():
    assert check_if_hits(3, 9, f1) == True


def test_check_if_hits5():
    assert check_if_hits(8, 9, f1) == False


def test_check_if_hits6():
    assert check_if_hits(4, 5, f1) == False


def test_check_if_hits7():
    assert check_if_hits(1, 1, f1) == False


def test_check_if_hits8():
    assert check_if_hits(2, 4, f1) == False


def test_hit1():
    (actual, s) = hit(3, 3, f1)
    actual.sort()
    expected = [(3, 3, False, 4, {(3, 3)}), (8, 1, True, 3, set()), (2, 1, False, 3, set()), (3, 9, False, 2, set()),
                (1, 7, True, 2, set()), (7, 5, True, 2, set()), (9, 9, True, 1, set()), (6, 9, True, 1, set()),
                (0, 3, True, 1, set()), (0, 0, True, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (3, 3, False, 4, {(3, 3)}))


f2 = [(3, 3, False, 4, {(3, 3)}), (8, 1, True, 3, set()), (2, 1, False, 3, set()), (3, 9, False, 2, set()),
      (1, 7, True, 2, set()), (7, 5, True, 2, set()), (9, 9, True, 1, set()), (6, 9, True, 1, set()),
      (0, 3, True, 1, set()), (0, 0, True, 1, set())]


def test_hit2():
    (actual, s) = hit(4, 3, f2)
    actual.sort()
    expected = [(3, 3, False, 4, {(3, 3), (4, 3)}), (8, 1, True, 3, set()), (2, 1, False, 3, set()),
                (3, 9, False, 2, set()), (1, 7, True, 2, set()), (7, 5, True, 2, set()), (9, 9, True, 1, set()),
                (6, 9, True, 1, set()), (0, 3, True, 1, set()), (0, 0, True, 1, set())]
    expected.sort()
    assert (actual, s) == (expected, (3, 3, False, 4, {(3, 3), (4, 3)}))


f3 = [(3, 3, False, 4, {(3, 3), (4, 3)}), (8, 1, True, 3, set()), (2, 1, False, 3, set()), (3, 9, False, 2, set()),
      (1, 7, True, 2, set()), (7, 5, True, 2, set()), (9, 9, True, 1, set()), (6, 9, True, 1, set()),
      (0, 3, True, 1, set()), (0, 0, True, 1, set())]


def test_hit3():
    (actual, s) = hit(0, 0, f3)
    actual.sort()
    expected = [(3, 3, False, 4, {(3, 3), (4, 3)}), (8, 1, True, 3, set()), (2, 1, False, 3, set()),
                (3, 9, False, 2, set()), (1, 7, True, 2, set()), (7, 5, True, 2, set()), (9, 9, True, 1, set()),
                (6, 9, True, 1, set()), (0, 3, True, 1, set()), (0, 0, True, 1, {(0, 0)})]
    expected.sort()
    assert (actual, s) == (expected, (0, 0, True, 1, {(0, 0)}))


f4 = [(3, 3, False, 4, {(3, 3), (4, 3)}), (8, 1, True, 3, set()), (2, 1, False, 3, set()), (3, 9, False, 2, set()),
      (1, 7, True, 2, set()), (7, 5, True, 2, set()), (9, 9, True, 1, set()), (6, 9, True, 1, set()),
      (0, 3, True, 1, set()), (0, 0, True, 1, {(0, 0)})]


def test_hit4():
    (actual, s) = hit(7, 6, f4)
    actual.sort()
    expected = [(3, 3, False, 4, {(3, 3), (4, 3)}), (8, 1, True, 3, set()), (2, 1, False, 3, set()),
                (3, 9, False, 2, set()), (1, 7, True, 2, set()), (7, 5, True, 2, {(7, 6)}), (9, 9, True, 1, set()),
                (6, 9, True, 1, set()), (0, 3, True, 1, set()), (0, 0, True, 1, {(0, 0)})]
    expected.sort()
    assert (actual, s) == (expected, (7, 5, True, 2, {(7, 6)}))


f5 = [(3, 3, False, 4, {(3, 3), (4, 3)}), (8, 1, True, 3, set()), (2, 1, False, 3, set()), (3, 9, False, 2, set()),
      (1, 7, True, 2, set()), (7, 5, True, 2, {(7, 6)}), (9, 9, True, 1, set()), (6, 9, True, 1, set()),
      (0, 3, True, 1, set()), (0, 0, True, 1, {(0, 0)})]


def test_hit5():
    (actual, s) = hit(9, 9, f5)
    actual.sort()
    expected = [(3, 3, False, 4, {(3, 3), (4, 3)}), (8, 1, True, 3, set()), (2, 1, False, 3, set()),
                (3, 9, False, 2, set()), (1, 7, True, 2, set()), (7, 5, True, 2, {(7, 6)}), (9, 9, True, 1, {(9, 9)}),
                (6, 9, True, 1, set()), (0, 3, True, 1, set()), (0, 0, True, 1, {(0, 0)})]
    expected.sort()
    assert (actual, s) == (expected, (9, 9, True, 1, {(9, 9)}))


def test_are_unsunk_ships_left1():
    f_ausl = [(6, 1, True, 4, set()), (0, 5, True, 3, set()), (2, 6, True, 3, set()), (8, 8, False, 2, set()),
              (4, 2, True, 2, set()), (5, 9, False, 2, set()), (0, 2, True, 1, set()), (2, 3, True, 1, set()),
              (5, 7, True, 1, set()), (2, 1, True, 1, set())]

    assert are_unsunk_ships_left(f_ausl) == True


def test_are_unsunk_ships_left2():
    f_ausl = [(6, 1, True, 4, set()), (0, 5, True, 3, {(0, 5), (0, 6), (0, 7)}), (2, 6, True, 3, set()),
              (8, 8, False, 2, set()), (4, 2, True, 2, set()), (5, 9, False, 2, set()), (0, 2, True, 1, set()),
              (2, 3, True, 1, set()), (5, 7, True, 1, set()), (2, 1, True, 1, set())]

    assert are_unsunk_ships_left(f_ausl) == True


def test_are_unsunk_ships_left3():
    f_ausl = [(6, 1, True, 4, set()), (0, 5, True, 3, {(0, 5), (0, 6), (0, 7)}),
              (2, 6, True, 3, {(2, 6), (2, 7), (2, 8)}),
              (8, 8, False, 2, {(8, 8), (9, 8)}), (4, 2, True, 2, {(4, 2), (4, 3)}), (5, 9, False, 2, {(5, 9), (6, 9)}),
              (0, 2, True, 1, {(0, 2)}), (2, 3, True, 1, {(2, 3)}), (5, 7, True, 1, {(5, 7)}),
              (2, 1, True, 1, {(2, 1)})]

    assert are_unsunk_ships_left(f_ausl) == True


def test_are_unsunk_ships_left4():
    f_ausl = [(6, 1, True, 4, set()), (0, 5, True, 3, set()), (2, 6, True, 3, set()), (8, 8, False, 2, set()),
              (4, 2, True, 2, set()), (5, 9, False, 2, set()), (0, 2, True, 1, set()), (2, 3, True, 1, set()),
              (5, 7, True, 1, set()), (2, 1, True, 1, set())]

    assert are_unsunk_ships_left(f_ausl) == True


def test_are_unsunk_ships_left5():
    f_ausl = [(6, 1, True, 4, {(6, 1), (6, 2), (6, 3), (6, 4)}), (0, 5, True, 3, set()), (2, 6, True, 3, set()),
              (8, 8, False, 2, set()), (4, 2, True, 2, set()), (5, 9, False, 2, set()), (0, 2, True, 1, set()),
              (2, 3, True, 1, set()), (5, 7, True, 1, set()), (2, 1, True, 1, set())]

    assert are_unsunk_ships_left(f_ausl) == True


def test_are_unsunk_ships_left6():
    f_ausl = [(6, 1, True, 4, {(6, 1), (6, 2), (6, 4)}), (0, 5, True, 3, {(0, 5), (0, 6), (0, 7)}),
              (2, 6, True, 3, {(2, 6), (2, 7), (2, 8)}), (8, 8, False, 2, {(8, 8), (9, 8)}),
              (4, 2, True, 2, {(4, 2), (4, 3)}), (5, 9, False, 2, {(5, 9), (6, 9)}), (0, 2, True, 1, {(0, 2)}),
              (2, 3, True, 1, {(2, 3)}), (5, 7, True, 1, {(5, 7)}), (2, 1, True, 1, {(2, 1)})]

    assert are_unsunk_ships_left(f_ausl) == True


def test_are_unsunk_ships_left7():
    f_ausl = [(6, 1, True, 4, {(6, 1), (6, 2), (6, 3), (6, 4)}), (0, 5, True, 3, {(0, 5), (0, 6), (0, 7)}),
              (2, 6, True, 3, {(2, 6), (2, 7), (2, 8)}), (8, 8, False, 2, {(8, 8), (9, 8)}),
              (4, 2, True, 2, {(4, 2), (4, 3)}), (5, 9, False, 2, {(5, 9), (6, 9)}), (0, 2, True, 1, {(0, 2)}),
              (2, 3, True, 1, {(2, 3)}), (5, 7, True, 1, {(5, 7)}), (2, 1, True, 1, {(2, 1)})]

    assert are_unsunk_ships_left(f_ausl) == False
