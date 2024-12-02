# Leading Substrings
## Problem
Write a function that takes a string argument and returns a list of substrings of that string. Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.

### Questions
- Does it need to sort numbers?
- Does it need to account for empty strings?

## Example
```python
# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
```

### Clarifications
- No need to sort numbers
- No empty strings either

## Data
Data handled is string and list.

**Input**: String
**Output**: List

## Algorithm
1. Initialize empty string and list
2. Iterate through the string:
    - Append item to the string
    - Append string to the list
3. Return the list

## Code
```python
def leading_substrings(string):
    item = ""
    result = []
    for letter in string:
        item += letter
        result.append(item)
    return result
```