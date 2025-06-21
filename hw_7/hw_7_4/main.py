def common_elements():
    set_miltiplies_3 = {x for x in range(100) if x % 3 == 0}
    set_miltiplies_5 = {x for x in range(100) if x % 5 == 0}
    return set_miltiplies_3.intersection(set_miltiplies_5)


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
