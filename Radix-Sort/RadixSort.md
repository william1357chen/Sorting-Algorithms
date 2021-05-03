# Radix Sort
Radix Sort is one special algorithm. There is one major differnce between radix sort and all the other sorting algorithms in this review unit. Radix sort is not a comparison sorting algorithms, meaning it doesn't sort by comparing integers. For comparison sorting algorithms, they cannot perform better than O(nlogn) in the average case, but radix sort could potentially do better than that, if the range of what we are sorting is small. For instance, if we want to sort employees based on age, we can assume the range is 0~199, and the time complexity will be `T(n) = 3n + C`

## Implementation
To understand Radix Sort, we have to first talk about **Counting Sort**

### Counting Sort
Check here for [Counting Sort](Counting-Sort/CountingSort.md)

The idea of Radix Sort is to perform **Counting Sort** on each digit of the elements in the array. For instance, integers of range 0~999 have maximum 3 digits in base 10 so we will perform **Counting Sort** 3 times with 10 buckets. Another example will be English words no more than 5 characters, we will perform **Counting Sort** 5 times with 26 buckets. 

We have to define some variables for us to clearly understand Radix Sort:

* n = number of elements in array
* d = number of digits of max element
* b = base/radix of numbers, or the range of elements in the array. For integers we use base 10 and for alphabets we use base 26. 

If you understand everything until now, we can sum Radix Sort in one sentence:
```
Radix Sort is performing d passes of counting sort for each digit with buckets of size b.
```
### Important Note
We have to make sure that Counting Sort is **stable** for Radix Sort to work!
___

## Time Complexity

Remember:
* n = number of elements in array
* d = number of digits of max element
* b = base/radix of numbers. Here we use base 10.
### Best, Average, Worst Case O(d(n+b))
The time complexity of Counting Sort is O(n+k), which `k` being the range of elements in the array, which is the same as `b` is radix sort. We perform counting sort `d` times, so time complexity is O(d(n+b)). We summarize the time complexity to O(kn) for simplicity, for the case where the base/radix is small like base 10 `b = 10`. In O(kn), `k = d`

___
## Space Complexity O(n+b)
The space complexity for **Counting Sort** is O(n+k), which `k = b` being the base/radix. Here we simplified it to use `k`, but this is kind of misleading. Note that although `n` is the same for time and space complexity, being the number of elements in the array, `k = d` in time complexity and `k = b` in space complexity. To summarize:

* O(kn) time complexity `k = d`
* O(n+k) space complexity `k = b`