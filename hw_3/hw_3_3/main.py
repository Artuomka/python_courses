def list_to_lists(input_list):
    if len(input_list) == 0:
        return [[], []]
    middle_index = int((len(input_list) + 1) // 2)

    first_list = input_list[:middle_index]
    second_list = input_list[middle_index:]
    return [first_list, second_list]


fisrt_test_list = [1, 2, 3, 4, 5, 6]
second_test_list = [1, 2, 3]
third_test_list = [1, 2, 3, 4, 5]
fourth_test_list = [1]
fifth_test_list = []

print("First list unchanged: ", fisrt_test_list)
print("First list changed: ", list_to_lists(fisrt_test_list))

print("\n")

print("Second list unchanged: ", second_test_list)
print("Second list changed: ", list_to_lists(second_test_list))

print("\n")

print("Third list unchanged: ", third_test_list)
print("Third list changed: ", list_to_lists(third_test_list))

print("\n")

print("Fourth list unchanged: ", fourth_test_list)
print("Fourth list changed: ", list_to_lists(fourth_test_list))

print("Fifth list unchanged: ", fifth_test_list)
print("Fifth list changed: ", list_to_lists(fifth_test_list))
