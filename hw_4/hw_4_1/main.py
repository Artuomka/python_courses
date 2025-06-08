def list_zeros_to_end(input_list):
    if not input_list:
        return input_list

    non_zero_list = [value for value in input_list if value]
    zero_list = [value for value in input_list if not value]

    return non_zero_list + zero_list


fisrt_test_list = [0, 1, 0, 12, 3]
second_test_list = [0]
third_test_list = [1, 0, 13, 0, 0, 0, 5]
fourth_test_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print("First list unchanged: ", fisrt_test_list)
print("First list changed: ", list_zeros_to_end(fisrt_test_list))

print("\n")

print("Second list unchanged: ", second_test_list)
print("Second list changed: ", list_zeros_to_end(second_test_list))

print("\n")

print("Third list unchanged: ", third_test_list)
print("Third list changed: ", list_zeros_to_end(third_test_list))

print("\n")

print("Fourth list unchanged: ", fourth_test_list)
print("Fourth list changed: ", list_zeros_to_end(fourth_test_list))
