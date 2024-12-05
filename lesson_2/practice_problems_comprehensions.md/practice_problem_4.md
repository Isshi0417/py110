# Practice Problem 4
## Problem
Given the following data structure, write some code that defines a dictionary where the key is the first item in each sublist, and the value is the second.

```python
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]
```

## Solution
```python
dictionary = {item[0] : item[1] for item in lst}
print(dictionary)
```