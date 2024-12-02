# Unique Elements
## Problem
From two list arguments, determine the elements that are unique to the first list. The return value should be a set.

## Example
```python
list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})
```

## Data
Data handled is list and set.

**Input**: List
**Output**: Set

## Algorithm
1. Convert lists to set
2. Return the unique values in list1

## Code
```python
def unique_from_first(list1, list2):
    return set(list1) - set(list2)
```