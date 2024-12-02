# Double Char (Part 1)
## Problem
Write a function that takes a string, doubles every character in the 
string, then returns the result as a new string.

## Example
```python
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
```

## Data
Data handled is explicitly strings.

**Input: String** 
**Output: String**

## Algorithm
1. Initialize empty string
2. Iterate through each character:
    - Append to the empty string twice
3. Return empty string

## Code
```python
def repeater(str):
    result = ""
    for character in str :
        result += character
        result += character
    return result
```