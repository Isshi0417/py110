# Practice Problem 9
## Problem
**This problem may prove challenging**. Try it, but don't stress about it. If you don't solve it in 20 minutes, you can look at the answer.

Given the following data structure, write some code to return a list that contains only the dictionaries where all the numbers are even.

```python
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
```

## Solution
```python
def all_even(dictionary):
    for values in dictionary.values():
        if not all([num % 2 == 0 for num in values]):
            return False

    return True

result = [val for val in lst if all_even(val)]
print(result)
```