"""
This is the implementation of Counting Sort on an array with a spefic range of integers.

There are two ways of doing Counting Sort, either stable and not in-place, or unstable and in-place.
Being stable and not in-place is perferred since we need a stable Counting sort for Radix Sort to work
"""

"""
In place and not stable
Time complexity: O(n+k)
Space complexity: O(k)
The range is set for integers 0 ~ 9.
"""


def unstable_count_sort(array):
    n = len(array)
    k = 10
    buckets = [0] * k
    # Fill buckets with number of occurances of each key
    for i in array:
        buckets[i] += 1
    # Sort the array by inputting elements depending on
    # the occurances of each key, and do it from key 0 to last key
    # Unstable since the order of elements in array is losted
    key = 0
    for i in range(n):
        if buckets[key] == 0:
            key += 1
            continue
        array[i] = key
        buckets[key] -= 1


"""
Not in-place but stable
Time complexity: O(n+k)
Space complexity: O(n+k)
The range is set for integers 0 ~ 9.
"""


def stable_count_sort(array):
    n = len(array)
    k = 10
    buckets = [0] * k
    # Fill buckets with number of occurances of each key
    for i in array:
        buckets[i] += 1
    # Find ending position of each key
    for i in range(1, k):
        buckets[i] += buckets[i - 1]
    # Find starting position of each key
    for i in range(k - 1, -1, -1):
        if i == 0:
            buckets[i] = 0
            continue
        buckets[i] = buckets[i - 1]
    # Sort the array stably by referencing the buckets
    result = [0] * n
    for i in array:
        result[buckets[i]] = i
        buckets[i] += 1
    # Mutate array by copying all elements of result into it
    for i in range(n):
        array[i] = result[i]


# A more dynamic version of count sort that find the range
# Code from GeekforGeeks
def count_sort(array):
    n = len(array)
    min_element = max(array)
    max_element = min(array)
    # Finding the range of elements
    k = range_of_elements = max_element - min_element + 1
    buckets = [0] * range_of_elements
    # Finding the number of occurances of each key
    for i in array:
        key = i - min_element
        buckets[key] += 1
    # Calculating the ending position of each key in bucket
    for i in range(1, k):
        buckets[i] += buckets[i - 1]
    result = [0] * n
    # building output array from the end positions of each key
    for i in range(n - 1, -1, -1):
        key = array[i] - min_element
        position = buckets[key] - 1
        result[position] = array[i]
        buckets[key] -= 1
    # Mutate array by copying all elements of result into it
    for i in range(n):
        array[i] = result[i]
