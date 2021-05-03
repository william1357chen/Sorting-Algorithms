# Insertion Sort

## Implementation
Insertion Sort is similar to sorting a hand of cards. The array will be divided into two parts: the sorted part at the left, and the unsorted part at the right. Values for the unsorted part of the array will be picked and **inserted** into the correct position of the sorted part.
___

## Time Complexity
### Best Case Ω(n)
Scenario: When the array is already sorted
### Average Case Θ(n<sup>2</sup>)
<br/>

### Worst Case O(n<sup>2</sup>)
Scenario: When the array is reversely sorted

___

## Worst Case Space Complexity O(1)
The sorting algorithm is done in-place
___

## Why is Insertion Sort Better than Bubble Sort?
To generalize, Insertion Sort is on average twice as fast than Bubble Sort.

Bubble Sort is bubbling up the maximum value of the unsorted left part to the sorted right part. Insertion Sort is inserting a value in the unsorted right part into the sorted left part. On average, inserting a value will land in the middle of the sorted left part, where as on averge bubbling up the maximum value will always iterate through the entire unsorted left part.

Additional Resource: [Link](https://stackoverflow.com/questions/17270628/insertion-sort-vs-bubble-sort-algorithms)
___

Reference:[Link](https://www.youtube.com/watch?v=i-SKeOcBwko&t=560s)