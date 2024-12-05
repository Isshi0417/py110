# Practice Problem 3
## Problem
Given the following data structure, return a **new** list with the same structure, but with the values in each sublist ordered in ascending order **as strings**. Use a comprehension if you can.

```python
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
```

## Solution
```python
sorted_list = [sorted(sorted_items, key=str) for sorted_items in lst]
print(sorted_list)
```