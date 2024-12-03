# Remove Consecutive Duplicates
## Problem
Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. Return the refined sequence.

## Example
```python
original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
```

## Data
Data handled are lists.

**Input**: List
**Output**: List

## Algorithm
1. Initialize empty list
2. Iterate through the list:
    - If the element is not in the empty list:
        - Add to it
3. Return the result

## Code
```python
def unique_sequence(numbers):
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result
```