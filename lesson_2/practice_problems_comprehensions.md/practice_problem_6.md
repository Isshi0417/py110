# Practice Problem 6
## Problem
Given the following data structure, return a new list identical in structure to the original, but with each number incremented by `1`. Do not modify the original data structure. Use a comprehension.

```python
lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
```

## Solution
```python
def increment(dictionary):
    return {key: value + 1 for key,value in dictionary.items()}

result = [increment(dictionary) for dictionary in lst]
print(result)
```