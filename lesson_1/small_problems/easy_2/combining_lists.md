# Combining Lists
## Problem
Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.

### Notes
- Sets can only contain unique values and order doesn't matter
- Convert lists to sets

## Example
```python
print(union([1,3,5], [3,6,9]) == {1, 3, 5, 6, 9})   # True
```

## Data
Data types handled are strictly lists and sets.

**Input: List**
**Output: List**

## Algorithm
1. Initialize empty list.
2. Iterate over list_1:
    - Add each value to the empty list
3. Iterate over list_2:
    - Add each value to the empty list
4. Convert empty list to set
5. Return set

## Code
```python
def union(list_1, list_2):
    blank = []
    for item in list_1:
        blank.append(item)
    for item in list_2:
        blank.append(item)

    return set(blank)
```