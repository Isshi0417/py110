# Double Char (Part 2)
## Problem
Write a function that takes a string, doubles every consonant in the 
string, and returns the result as a new string. The function should 
not double vowels ('a', 'e', 'i', 'o', 'u'), digits, punctuation, or 
whitespace.

You may assume only ASCII characters will be included in the argument.

## Example
```python
# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
```

## Data
Data handled are strictly strings.

**Input**: String
**Output**: String

## Algorithm
1. Initialize empty string
2. Check if not alphabet or vowels:
    - Add to string once
   Else:
    - Add to string twice
3. Return empty string

## Code
```python
def double_consonants(str):
    result = ""
    for character in str:
        if (not character.isalpha() or character == "a" or
        character == "e" or character == "i" or character == "o" or
        character == "u"):
            result += character
        else:
            result += character
            result += character
    return result
```