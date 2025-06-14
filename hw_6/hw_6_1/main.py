import string


def print_letters_diapason(from_to_letters):
    borders = from_to_letters.split("-")

    available_letters = string.ascii_letters

    start_range = available_letters.index(borders[0])
    end_range = available_letters.index(borders[1])

    if end_range < start_range:
        start_range, end_range = end_range, start_range

    return available_letters[start_range : end_range + 1]


first_test_range = "a-c"
second_test_range = "a-a"
third_test_range = "s-H"
fourth_test_range = "a-A"

print(print_letters_diapason(first_test_range))
print(print_letters_diapason(second_test_range))
print(print_letters_diapason(third_test_range))
print(print_letters_diapason(fourth_test_range))
