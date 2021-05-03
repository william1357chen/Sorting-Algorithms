# Radix Sort
Radix Sort is one special algorithm. There is one major differnce between radix sort and all the other sorting algorithms in this review unit. Radix sort is not a comparison sorting algorithms, meaning it doesn't sort by comparing integers. For comparison sorting algorithms, they cannot perform better than O(nlogn) in the average case, but radix sort could potentially do better than that, if the range of what we are sorting is small. For instance, if we want to sort employees based on age, we can assume the range is 0~199, and the time complexity will be `T(n) = 3n + C`

## Implementation
To understand Radix Sort, we have to first talk about **Counting Sort**

## Counting Sort


The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. Radix sort takes advantage of the fact that integers have a finite number of digits. 
1. We will first find the number of digits in the biggest number of the array. If there are K digits in the biggest number then we will need to perfom K number of passes. 
2. Create 10 buckets labeled 0 - 9
3. For each pass, put all elements of the array in the respected bucket by checking the value of their currently compared digit. 
4. Now when we put the elements back into the array starting from bucket 0, the elements will be sorted by their current digit. 
5. Repeat for K passes and now the array is sorted. 
___

## Time Complexity
`n` is the number of elements in the array and `k` is the number of digits the maximum element has, which requires K passes through the entire array. 

To be more specific, let's say
* n = number of elements in array
* d = number of digits of max element
* b = base/radix of numbers. Here we use base 10.
### Best Case Ω(kn)
<br/>

### Average Case Θ(kn)
<br/>

### Worst Case O(kn)
<br/>

___
## Space Complexity O(n+k)
Note that although `n` is the same for space complexity, being the number of elements in the array, `k` is actually the *radix* of what we are sorting. For example, if we use base 10 decimals, the *radix* is 10 so `k` is 10. For alphabets, the *radix* is 26 so `k` is 26. The space complexity comes from the `k=10` buckets from 0 - 9, storing `n` elements for each pass. Therefore, space complexity is O(n+k). Again, `k` is the number of buckets, and `n` is the number of elements stored in the bucket for each pass.
