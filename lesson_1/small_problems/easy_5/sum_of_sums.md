# Sum of Sums
## Problem
Write a function that takes a list of numbers and returns the sum of the sums of each leading subsequence in that list. Examine the examples to see what we mean. You may assume that the list always contains at least one number.

## Example
```python
print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True
```
## Data
Data handled are lists and integers.

**Input**: List
**Output**: Integer

## Algorithm
1. Initialize total sum
2. Initialize sum
3. Iterate through each number
4. Add the running sum to the sum
5. Add to total sum
6. Return the total sum

## Code
```python
def sum_of_sums(numbers):
    total_sum = 0
    sum = 0
    for number in numbers:
        sum += number
        total_sum += sum
    return total_sum
```