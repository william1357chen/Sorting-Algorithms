# Counting Sort
Counting Sort is a sorting technique based on keys in a specific range, like integers 0 - 9. We count how many of each integer 0 - 9 appears in the array, and then determine each integer's starting position in the array by counting how many cells are taken up by the integers less than it.

Here's an example on an array with only integers 0 - 3. `n = 6` is the number of elements in the array, and `k = 4` is the range of integers we can have in the array.

|   1| 0  | 3  |1   | 3 | 1 |
|---|---|---|---|---|---|

___
1. We will make `k = 4` *buckets* (as an array of size `k`) that stores the occurances of each integer 0 - 3, with key as the index. 

|k|   0| 1  | 2  |3  
|---|---|---|---|---|
|occurances|1|3|0|2
___
2. We then determine each integer's ending position in the *buckets* by adding its number of occurances with the previous number's ending position.

|k|   0| 1  | 2  |3  
|---|---|---|---|---|
|ending position|1|4|4|6
___
3. We then determine each integer's starting position in the *buckets* by getting the ending position of the previous number using shifting. The last number will wrap back around.

|k|   0| 1  | 2  |3  
|---|---|---|---|---|
|starting position|0|1|4|4

4. Now, we sort the array by inputing keys of either 0 - 3 depending on the starting positions of keys in our buckets.

|  0| 1  | 1  |1   | 3 | 3 |
|---|---|---|---|---|---|

___
## Alternate In-Place Counting Sort
Question: Why can't we simply get the number of occurances of each key and sort the array by inputting the occurances of each key in order starting from key 0?

Here's the example of the question:

|   1| 0  | 3  |1   | 3 | 1 |
|---|---|---|---|---|---|
___
1. We will make `k = 4` *buckets* (as an array of size `k`) that stores the occurances of each integer 0 - 3, with key as the index. 

|k|   0| 1  | 2  |3  
|---|---|---|---|---|
|occurances|1|3|0|2

2. We simply fill the array with the number of occurances of each key in order starting from key 0. So starting at the 0th index of the array, we fill in one 0 and starting at the 1th index of the array, we fill in three 1s. This will sort the array **in place**, taking only space complexity of **O(k)**.  

|  0| 1  | 1  |1   | 3 | 3 |
|---|---|---|---|---|---|
___
### So Why is this Bad?
For stability concerns, this technique of counting sort is **unstable**, meaning the order of the same elements in the array will not withhold after sorting. 

|   1| 0  | 3  |1   | 3 | 1 |
|---|---|---|---|---|---|

In the example above, indices 0 and 3 are both 1s but for a **stable** sorting technique, the 1 on index 1 must be before the 1 on index 3 after sorting. 

For other sorting algorithms to utlize counting sort like *Radix Sort*, it is important for countint sort to be a stable sorting algorithm. 
