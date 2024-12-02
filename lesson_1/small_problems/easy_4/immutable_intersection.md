# Immutable Intersection
## Problem
Transform two lists into frozen sets and find their common elements.

## Example
```python
list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True
```

## Data
Data handled is a list and frozen set.

**Input**: List
**Output**: Frozen Set

## Algorithm
1. Convert the list to frozen set
2. Return the common element

## Code
```python
def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)
```