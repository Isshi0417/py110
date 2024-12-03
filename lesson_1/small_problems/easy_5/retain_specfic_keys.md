# Retain Specific Keys
## Problem
Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for the specified keys.

## Example
```python
input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True
```

## Data
Data handled is dictionary.

**Input**: Dictionary
**Output**: Dictionary

## Algorithm
1. Initialize empty dictionary
2. Check if key exists in the key list:
    - Add the key, value to the empty dictionary
3. Return the dictionary

```python
def keep_keys(dictionary, keys):
    result = {}
    for key in keys:
        if key in dictionary:
            result[key] = dictionary[key]
    return result
```