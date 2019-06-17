# Given an array of integers and a number k, where 1 <= k <= length of the array,
# compute the maximum values of each subarray of length k.
#
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
#
#     10 = max(10, 5, 2)
#     7 = max(5, 2, 7)
#     8 = max(2, 7, 8)
#     8 = max(7, 8, 7)
#
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
# You can simply print them out as you compute them.


def create_subarrays(array, k):
    response_array = []
    for i in range(len(array)):
        subarray = array[i:k+i]
        if len(subarray) < k:
            break
        else:
            response_array.append(max(subarray))
    print(response_array)


if __name__ == '__main__':
    print('In the main method')
    array_to_use = [10, 5, 2, 7, 8, 7]
    k = 3
    create_subarrays(array_to_use, k)
