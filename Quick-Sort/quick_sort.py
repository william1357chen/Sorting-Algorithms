"""
This is the implementation of Quick Sort on an array of integers.
The function sorts an input list of integers by mutating it.
"""
import random 

def quick_sort(array, low, high):
    if low >= high:
        return
    p_index = random_partition(array, low, high)
    quick_sort(array, low, p_index - 1)
    quick_sort(array, p_index + 1, high)


# find a random value in array as pivot to maintain average case O(nlogn)
def random_partition(array, low, high):
    p_index = random.randint(low, high)
    array[high], array[p_index] = array[p_index], array[high]
    return right_pivot_partition(array, low, high)

# choose the element at the low position as the pivot
def left_pivot_partition(array, low, high):
    pivot = array[low]
    p_index = high
    for i in range(high, low, -1):
        if array[i] > pivot:
            array[i], array[p_index] = array[p_index] = array[i]
            p_index -= 1 
    array[high], array[p_index] = array[p_index] = array[high]
    return p_index

# choose the element at the high position as the pivot
def right_pivot_partition(array, low, high):
    pivot = array[high]
    p_index = low
    for i in range(low, high):
        if array[i] <= pivot:
            array[i], array[p_index] = array[p_index], array[i]
            p_index += 1 
    array[high], array[p_index] = array[p_index], array[high]
    return p_index
