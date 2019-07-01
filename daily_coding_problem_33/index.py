# This problem was asked by Microsoft.
#
# Compute the running median of a sequence of numbers. That is, given a stream of numbers,
# print out the median of the list so far on each new element.
#
# Recall that the median of an even-numbered list is the average of the two middle numbers.
#
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
#
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

import math


def calculate_median(array):
    array.sort()
    print(array)
    array_length = len(array)
    if array_length % 2 == 0:
        first_middle_index = int((array_length / 2) - 1)
        seccond_middle_index = int(((array_length / 2) + 1) - 1)
        first_middle = array[first_middle_index]
        last_middle = array[seccond_middle_index]
        median = (first_middle + last_middle) / 2
    else:
        index = int(math.ceil(array_length / 2) -1)
        median = array[index]
    return median


if __name__ == '__main__':
    numbers_array = []
    median_array = []
    while True:
        number = input('Enter a number:')
        number = float(number)
        if number < 0:
            break

        numbers_array.append(number)
        actual_median = calculate_median(numbers_array)
        median_array.append(actual_median)
        print(str(actual_median))

    print('-----------------')
    print(numbers_array)
    print(median_array)
