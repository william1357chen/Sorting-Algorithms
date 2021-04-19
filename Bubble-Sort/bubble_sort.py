"""
This is the implementation of Bubble Sort on an array of integers.
The function sorts an input list of integers by mutating it.
"""

def bubble_sort(array: list) -> None:
    n = len(array)
    # we need n-1 passes to gurantee sorted. n-1 because the min value will sit
    # at 0 automatically after n-1 passes so no need for another pass
    for i in range(n - 1):
        # have a flag check for if there are no swaps, meaning array is sorted
        flag = 0
        # one pass. we don't have to enter the sorted right part of the array
        # so we have n - i - 1
        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                flag = 1
        if flag == 0:
            break

