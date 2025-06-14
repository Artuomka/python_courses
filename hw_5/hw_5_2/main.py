question = "y"
while question == "y" or question == "yes":
    first_number = float(input("Please enter a first number: "))
    operation = input("Please enter an ariphmetic operation: ")

    if operation not in ["+", "-", "*", "/"]:
        print("Unknown operation!")
    else:
        second_number = float(input("Please enter a second number: "))

        if operation == "+":
            result = first_number + second_number
            print(result)

        elif operation == "-":
            result = first_number - second_number
            print(result)

        elif operation == "*":
            result = first_number * second_number
            print(result)

        elif operation == "/":
            if second_number != 0:
                result = first_number / second_number
                print(result)
            else:
                print("You can not divide by zero!")

    question = input("\nDo you want to continue? (y/n): ")
