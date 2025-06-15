def multiply_input(input_number):
    if input_number <= 9:
        return input_number

    result = 1
    for digit in str(input_number):
        result = result * int(digit)
    return multiply_input(result)


user_input = int(input("Input number: "))
print(multiply_input(user_input))
