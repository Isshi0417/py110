# Merge Sets
## Problem
Given two lists, convert them to sets and return a new set which is the union of both sets.

## Example
```python
list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True
```

## Data
Data handled are list and set.

**Input**: List
**Output**: Set


## Algorithm
1. Concatenate list
2. Convert to a set

## Code
```python
def merge_sets(list1, list2):
    return set(list1 + list2)
```