def difference(*args):
    if len(args) == 0:
        return 0

    max_number = max(args)
    min_number = min(args)
    return round(max_number - min_number, 2)


assert difference(1, 2, 3) == 2, "Test1"
assert difference(5, -5) == 10, "Test2"
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, "Test3"
assert difference() == 0, "Test4"
print("OK")
