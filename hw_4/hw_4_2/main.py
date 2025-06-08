def sum_even_indexes(input_list):
    if not input_list:
        return 0
    result_sum = 0
    for index, value in enumerate(input_list):
        if index % 2 == 0:
            result_sum += value

    return result_sum * input_list[-1]


fisrt_test_list = [1, 3, 5]
second_test_list = [6]
third_test_list = []

print("First list: ", fisrt_test_list)
print("First list result: ", sum_even_indexes(fisrt_test_list))

print("\n")

print("Second list: ", second_test_list)
print("Second list result: ", sum_even_indexes(second_test_list))

print("\n")

print("Third list: ", third_test_list)
print("Third list result: ", sum_even_indexes(third_test_list))
