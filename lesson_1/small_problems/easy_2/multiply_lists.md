# Multiply Lists
## Problem
Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains the product of each pair of numbers from the arguments that have the same index. You say assume that the arguments contain the same number of elements.

### Note
- Take atw olists and retusn a new list that is the sum of the numbers.

## Example
```python
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
```

## Data
Data handled is strictly lists.

**Input: List**
**Output: List**

## Algorithm
1. Initialize empty list
2. Iterate as many times as the length of the list:
    - multiply the item of each list
    - append to empty list
3. Return empty list

## Code
```python
def multiply_list(list1, list2):
    blank = []
    for i in range(len(list1)):
        blank.append(list1[i] * list2[i])
    return blank
```