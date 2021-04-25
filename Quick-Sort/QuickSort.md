# Quick Sort

## Implementation
The quicksort algorithm is similar to merge sort in the sense that they are both divide and conquer algorithms. Quick sort picks an element as pivot, partitions the array so that elements less or equal to the pivot is to the left of the pivot, and elements greater than the pivot is to the right of the pivot. Lastly, a perform quicksort again to the left of the pivot and the right of the pivot. 

There are mutliply ways of picking a pivot:

1. Always pick the first element of subarray
2. Always pick the last element of subarray
3. Pick a random element as pivot

How to partition the given array is the key and most complicated part of quicksort. If we choose to pick the last element of array as the pivot, we start at the 0th index of the array and have a p_index initilized at 0, which will be the position of where the pivot would be. We should have every element smaller than the pivot to the left of p_index and everything bigger to the right of p_index. Lastly, we will just swap the pivot to the correct index. Here is the pseudo code for partition.
```
partition(arr, low, high)
    pivot = arr[high]
    p_index = low
    
    for i at low to high - 1:
        if arr[i] less or equal pivot:
            swap arr[i] and arr[p_index]
            increment p_index so element is left of p_index
        else:
            # arr[i] is bigger than pivot so do nothing since arr[i] is right or at p_index 
    swap arr[high] with arr[p_index] since we want pivot to be at p_index

    return p_index 
```
---
## Time Complexity
### How to calculate the time complexity?
For me, I see quicksort has a recursion depth of O(logn), since it is dividing into halves til size of 1. Each recursive level of the recursion tree costs n (you will understand if you draw the recursion tree out and see what the size of the subarray is **partition** iterating through), so total runtime is recursion depth * cost of each recursion level = O(nlogn)


### Best Case Ω(nlogn)
Scenario: When every pivot picked creates a balanced partitioning, meaning we always pick the median of the array, so the array of size n is always divided to two subarrays of size n/2
### Average Case Θ(nlogn)

Scenario: If we implement picking a random pivot, we can almost gurantee average case O(nlogn) where the average of all possible partitions will be O(nlogn).

### Worst Case O(n<sup>2</sup>)
Scenario: When every pivot picked creates an unbalanced partitioning, meaning we always pick the max or min of the array, so the array of size n is divided to two subarrays of size n - 1 and size 1.

___
## Space Complexity

### How to calculate the space complexity?
Quicksort has a recursion depth of O(logn), and the partitions are done in place so no additional memory is needed. Therefore, quicksort requires O(logn) space on the call stack. 

### Best and Average Case O(logn)
Scenario: When every pivot picked creates a balanced partitioning or we implement picking a random pivot, The recursion tree of quick sort will go down to logn levels, which is the space complexity of quicksort, since quicksort mutates the array in place.

### Worst Case O(n)
Scenario: When every pivot picked creates an unbalanced partitioning, The recursion tree goes down to n levels, so O(n)