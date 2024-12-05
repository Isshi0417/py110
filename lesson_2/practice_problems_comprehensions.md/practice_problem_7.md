# Practice Problem 7
## Problem
Given the following data structure return a new list identical in structure to the original, but containing only the numbers that are multiples of 3.

```python
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
```
## Solution
```python
result = [[number for number in sublist if number % 3 == 0]
          for sublist in lst]
print(result)
```