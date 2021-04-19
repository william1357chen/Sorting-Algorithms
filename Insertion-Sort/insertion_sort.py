"""
This is the implementation of Insertion Sort on an array of integers.
The function sorts an input list of integers by mutating it.
"""

def insertion_sort(array: list) -> None:
    n = len(array)
    # let index 0 be the sorted part and right of that the unsorted part
    # n-1 passes will be conducted to insert all unsorted elements into sorted part
    for i in range(1, n):
        hole = i
        value = array[i]
        while(hole > 0 and value < array[hole - 1]):
            array[hole] = array[hole - 1]
            hole -= 1 
        array[hole] = value


