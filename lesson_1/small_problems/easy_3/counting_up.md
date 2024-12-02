# Counting Up
## Problem
Write a function that takes an integer argument and returns a list containing all integers between `1` and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

## Notes
- List should contain all values from 1 through the given integer
- Negative numbers don't need to be accounted for

## Example
```python
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
```

## Data
Data handled is explicitly integers.

**Input**: Integer
**Output**: Integer

## Algorithm
1. Initialize empty list
2. Iterate through the values of the integer
3. Append the integer to the list
4. Return the empty list

## Code
```python
def sequence(number):
    result = []
    for i in range(1, number + 1):
        result.append(i)
    return result
```