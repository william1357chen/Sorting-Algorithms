# Merge Sort

## Implementation
Merge Sort implements a divide and conquer strategy. Merge sort divides the array into halves, say that we sort the left half of the array first, and then sort the right half of the array. Now we have two sorted arrays, which we will then merge the two sorted left and right arrays back to the original array.
___
## Time Complexity
### How to calculate the time complexity?
For me, I see merge sort has a recursion depth of O(logn), since it is dividing into halves til size of 1. Each recursive level of the recursion tree costs n (you will understand if you draw the recursion tree out and see what the size of the subarray is **merge** iterating through), so total runtime is recursion depth * cost of each recursion level = O(nlogn)

There are no difference for Best, Average, and Worst Case Time Complexity since merge sort does the same thing for all three cases
### Best Case Ω(nlogn)
<br/>

### Average Case Θ(nlogn)
<br/>

### Worst Case O(nlogn)
<br/>

___
## Space Complexity
### How to calculate space complexity?
We know the recursion depth for merge sort is O(logn), and we know that merge has to make copies of left subarray and right subarray. Since, the left subarray will be recursed first, the right subarray's branches will not be called before left subarray, there will be O(logn) calls, which means there will be (n + n/2 + n/4 +...+ 1) = 2n - 1 memory for copying the array. Therefore, we have O(n) additional space required on the heap. Additionally, there are O(logn) resursive calls on the stack. O(n) outweighs O(logn) so merge sort requires O(n) space.

### Worst Space Complexity O(n)
