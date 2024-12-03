# Word to Digit
## Problem
Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.

## Example
```python
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
```

## Data
Data handled are dictionary and string.

**Input**: String
**Intermediate Step**: Dictionary
**Output**: String

## Algorithm
1. Initialize a constant with the numbers.
2. Initialize empty list
3. Iterate through the string and split:
    - Iterate through the list:
        - If the string is in the constant:
            - Replace with its corresponding number
            - Add to the empty list
        - Else:
            - Add to the empty list
4. Return the result

## Code
```python
def word_to_digit(message):
    NUMBERS = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    result = []
    lst = message.split(" ")
    for string in lst:
        if string in NUMBERS:
            result.append(NUMBERS[string])
        else:
            result.append(string)
    return " ".join(result)
```