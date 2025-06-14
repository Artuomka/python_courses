import string
import keyword


def is_valid_name(input_name):
    if not input_name:
        return False

    if input_name == "_":
        return True

    if input_name.strip("_") == "" and len(input_name) > 1:
        return False

    if input_name[0].isdigit():
        return False

    for letter in input_name:
        if (
            letter.isupper()
            or letter.isspace()
            or (letter in string.punctuation and letter != "_")
        ):
            return False

    if input_name in keyword.kwlist:
        return False

    return True


input_name = input("Please write vairble name for checking: ")

print(is_valid_name(input_name))
