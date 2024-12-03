# Inverting Dictionary
## Problem
Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its values become keys.

## Example
```python
print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True
```

## Data
Data handled is dictionary.

**Input**: Dictionary
**Output**: Dictionary

## Algorithm
1. Initialize empty dictionary
2. Iterate through the dictionary for each key, value:
    - Add to new dictionary such that value, key
3. Return the result

## Code
```python
def invert_dict(dictionary):
    result = {}
    for key, value in dictionary.items():
        result[value] = key
    return result
```