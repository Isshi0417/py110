# Halvsies
## Problem
Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list.

### Note
- Split the lists into two
- Find the middle point and split.

### Questions
- Do empty lists need to be accounted for?

## Example
```python
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
```

### Clarifications
- Empty lists need to be accounted for
- Single item lists need to be accounted for as well

## Data
Data implemented are strictly lists.

**Input: List**
**Output: List**

## Algorithm
1. Find the midpoint of the list
2. Append the first half
3. Append the second half
4. Return both lists

## Code
```python
def halvsies(numbers):
    half = (len(numbers) + 1) // 2
    first_half = numbers[:half]
    second_half = numbers[half:]
    return [first_half, second_half]
```
