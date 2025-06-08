import random


def random_list_from_list():
    random_list_length = random.randint(3, 10)
    random_list = []
    for i in range(random_list_length):
        random_list.append(random.randint(0, 1000))
    list_from_list = [random_list[0], random_list[2], random_list[-2]]
    return (random_list, list_from_list)


first_call_result = random_list_from_list()
print("First call randomed list: ", first_call_result[0])
print("First call list from random list: ", first_call_result[1], "\n")

second_call_result = random_list_from_list()
print("Second call randomed list: ", second_call_result[0])
print("Second call list from random list: ", second_call_result[1], "\n")

third_call_result = random_list_from_list()
print("Third call randomed list: ", third_call_result[0])
print("Third call list from random list: ", third_call_result[1], "\n")
