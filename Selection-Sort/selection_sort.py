"""
This is the implementation of Selection Sort on an array of integers.
The function sorts an input list of integers by mutating it.
"""
def selection_sort(array: list) -> None:
    # Loop til second last num since last num will be the max after second last comparison
    for i in range(len(array) - 1):
        # Find the minimum value in array[i+1:]
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        # Swap current iterating value with min of the remaining list
        array[i], array[min_index] = array[min_index], array[i]

