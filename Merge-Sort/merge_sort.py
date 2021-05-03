"""
This is the implementation of Merge Sort on an array of integers.
The function sorts an input list of integers by mutating it.
"""


def merge_sort(array):
    n = len(array)
    # base case: if the array has size 1, it is already sorted
    if n == 1:
        return

    # divide the array into two parts, the left and the right
    high = n
    low = 0
    mid = (high + low) // 2
    left_array = array[low:mid]
    right_array = array[mid:high]

    # recursively sort the left half of the array first
    merge_sort(left_array)
    # recursively sort the right half of the array
    merge_sort(right_array)
    # merge the sorted left and sorted right array into the original array
    merge(left_array, right_array, array)


# Merge two sorted arrays
def merge(left_array, right_array, array):
    left_length = len(left_array)
    right_length = len(right_array)
    i = (
        j
    ) = (
        k
    ) = 0  # i is counter for left, j is counter for right, and k is counter for array

    # comparing the values of left and right array and push the minimum in original array
    while i < left_length and j < right_length:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    # when right array's elements are all in array and left array still has elements
    while i < left_length:
        array[k] = left_array[i]
        i += 1
        k += 1
    # when left array's elements are all in array and right array still has elements
    while j < right_length:
        array[k] = right_array[j]
        j += 1
        k += 1
