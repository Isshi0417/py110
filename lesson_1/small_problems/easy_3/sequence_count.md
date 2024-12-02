# Sequence Count
## Problem
Create a function that takes two integers as arguments. The first argument is a count, and the second is the starting number of a sequence that your function will create. The function should return a list containing the same number of elements as the `count` argument. The value of each element should be a multiple of the starting number.

You may assume that `count` will always be an integer greater than or equal to 0. The starting number can be any integer. If the `count` is `0`, the function should return an empty list.

## Example
```python
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
```

## Data
Data handled is strictly integers.

**Input**: Integer
**Output**: Integer

## Algorithm
1. Initialize empty list
2. Check if count is 0:
    - Return empty list
3. Else:
    - for the length of count:
        - append sequence * current iteration
4. Return the result

## Code
```python
def sequence(count, sequence):
    result = []
    if count == 0:
        return result
    else:
        for i in range(1, count + 1):
            result.append(sequence * i)
    return result
```