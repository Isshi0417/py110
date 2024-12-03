# Delete Vowels
## Problem
Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.

### Notes
- Remove vowels from the string

### Questions
- Do numeric values also need to be incorporated?

## Example
```python
# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
```

## Data
Data handled is strictly strings.

**Input**: String
**Output**: String

## Algorithm
1. Declare a constant of vowels
2. Iterate through the string list:
    - Initialize empty string
    - Iterate through each letter:
        - If letter is not in constant:
            1. Add to empty string
    - Append the stripped word to the list
4. Return the result

## Code
```python
def remove_vowels(words):
    VOWELS = "aeiouAEIOU"
    result = []
    for word in words:
        stripped = ""
        for letter in word:
            if letter not in VOWELS:
                stripped += letter
        result.append(stripped)
    return result
```