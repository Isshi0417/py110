# Practice Problem 3
## Problem
Repeat problem 2, but this time, sort hte list as string values. Both the list passed to the sorting function and the returned list should contain numbers, not strings.

```python
lst = [10, 9, -6, 11, 7, -16, 50, 8]
```

## Solution
```python
print(sorted(lst, key=str))
print(sorted(lst, key=str, reverse=True))
```