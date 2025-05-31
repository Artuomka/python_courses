user_input = int(input("Please enter a 5-digit number: "))

fifth_digit = user_input % 10
fourth_digit = user_input // 10 % 10
third_digit = user_input // 100 % 10
second_digit = user_input // 1000 % 10
first_digit = user_input // 10000 % 10

reversed_digit = fifth_digit * 10000
reversed_digit += fourth_digit * 1000
reversed_digit += third_digit * 100
reversed_digit += second_digit * 10
reversed_digit += first_digit

print(reversed_digit)
