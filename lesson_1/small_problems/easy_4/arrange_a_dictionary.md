# Arrange a Dictionary
## Problem
Given a dictionary, return its keys sorted by the values associated with each key.

## Example
```python
my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
```

## Data
Data handled is list and dictionary.

**Input**: Dictionary
**Output**: List

## Algorithm
1. Initialize empty list
2. Sort the dictionary based on the second element of a dictionary item
3. Iterate through the key, value in the sorted dictionary
    - Append the key to the empty list
4. Return list

## Code
```python
def sort_dict(item):
    return item[1]

def order_by_value(dict):
    result = []
    sorted_dict = sorted(dict.items(), key = sort_dict)
    for key, value in sorted_dict:
        result.append(key)
    return result
```