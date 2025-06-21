def add_one(some_list):
    string_list = [str(number) for number in some_list]
    number_from_list = int("".join(string_list))
    result = number_from_list + 1
    return [int(digit) for digit in str(result)]


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"
print("ОК")
