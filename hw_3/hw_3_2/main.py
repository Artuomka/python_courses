def change_list_element_position(input_list):
    if len(input_list) <= 1:
        return input_list
    last_list_element = input_list.pop()
    input_list.insert(0, last_list_element)
    return input_list


first_test_list = [12, 3, 4, 10]
second_test_list = [1]
third_test_list = []
fourth_test_list = [12, 3, 4, 10, 8]

print("First list unchanged: ", first_test_list)
print("First list changed: ", change_list_element_position(first_test_list))

print("\n")

print("Second list unchanged: ", second_test_list)
print("Second list changed: ", change_list_element_position(second_test_list))

print("\n")

print("Third list unchanged: ", third_test_list)
print("Third list changed: ", change_list_element_position(third_test_list))

print("\n")

print("Fourth list unchanged: ", fourth_test_list)
print("Fourth list changed: ", change_list_element_position(fourth_test_list))
