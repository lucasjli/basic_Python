import random

num = list(random.choices(range(1, 51), k=100))

print(num)


def find_smallest(array, index=1, current_min=None):
    if current_min is None:
        current_min = array[0]

    if index == len(array):
        return current_min

    if array[index] < current_min:
        current_min = array[index]

    return find_smallest(array, index + 1, current_min)


smallest_number = find_smallest(num)

print(f"The smallest number in the list is: {smallest_number}")
