import pytest
from ipynb.fs.full.index import slices_of_pie, slices_eaten, time_for_breakfast, number_of_cooked_pancakes, line_of_hungry_patrons, fed_patrons

def test_find_first_dog_person():
    assert type(slices_of_pie) == type(1)
    assert type(slices_eaten) == type(1)
    assert slices_of_pie == 0
    assert slices_eaten == 6

def test_time_for_breakfast():
    assert type(time_for_breakfast) == type(1)
    assert time_for_breakfast == 1198
    assert number_of_cooked_pancakes == 5

def test_line_of_hungry_patrons():
    assert len(line_of_hungry_patrons) == 15
    assert len(fed_patrons) == 15
    assert line_of_hungry_patrons == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    assert fed_patrons == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
