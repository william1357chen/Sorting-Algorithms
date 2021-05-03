"""
This is the implementation of Radix Sort on an array of integers with a specific range.

b = 10
d = digits of max element in array

The function sorts an input list of integers by mutating it.
"""


def radix_sort(array):
    max_element = max(array)
    b = 10

    exp = 1
    while (max_element // exp) > 0:
        count_sort(array, exp)
        exp *= b


def count_sort(array, exp):
    n = len(array)
    b = 10
    buckets = [0] * b
    # Finding the number of occurances of each digit 0 ~ 9
    for i in array:
        digit = i // exp
        buckets[digit % 10] += 1
    # Calculating the ending position of each key in bucket
    for i in range(1, b):
        buckets[i] += buckets[i - 1]
    # building output array from the end positions of each key
    result = [0] * n
    for i in range(n - 1, -1, -1):
        digit = array[i] // exp
        key = digit % 10
        position = buckets[key] - 1
        result[position] = array[i]
        buckets[key] -= 1
    # Mutate array by copying all elements of result into it
    for i in range(n):
        array[i] = result[i]
