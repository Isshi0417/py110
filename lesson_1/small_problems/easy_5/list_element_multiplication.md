# List Element Multiplication
## Problem
Given two integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.

## Example
```python
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True
```

## Data
Data handled are lists and integers.

**Input**: List
**Intermediate Steps**: Integer
**Output**: List

## Algorithm
1. Initialize empty list
2. Iterate through the length of the list:
    - multiply the items
    - store in the list
3. Return the result

## Code
```python
def multiply_items(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] * list2[i])
    return result
```