# Practice Problem 3
## Problem
Given the following code, what will the final values of `a` and `b` be? Try to answer without running the code.

```python
a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a
```

## Solution
```python
a = 4
b = [3, 8]
lst = [4, [3, 8]]
```