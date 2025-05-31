user_input = int(input("Please enter a 4-digit number: "))

first_digit = user_input // 1000
second_digit = user_input // 100 % 10
third_digit = user_input // 10 % 10
fourth_digit = user_input % 10

print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)
