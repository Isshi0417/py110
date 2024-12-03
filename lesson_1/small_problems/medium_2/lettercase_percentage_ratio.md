# Lettercase Percentage Ratio
## Problem
Write a function that takes a string and returns a dictionary containing the following properties:

- the percentage of characters in the string that are lowercase letters
- the percentage of characters that are uppercase letters
- the percentage of characters that ar neither

All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.0", respectively. Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

## Example
```python
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
```

## Data
Data handled is integer and dictionary.

**Input**: String
**Output**: Dictionary

## Algorithm
1. Initialize lowercase and uppercase constants
2. Initialize count for each and set to 0
3. for each character in the string:
    - Check if the character is in lowercase:
        - increase count for lowercase number
    - Check if the character is in uppercase:
        - increase count for uppercase number
    - Else:
        - increase count for neither
4. Calculate percentage for each
5. Round to two decimal places
6. Add to dictionary
7. Return the dictionary

## Code
```python
def letter_percentages(string):
    LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result = {}
    lower_count, upper_count, neither_count = 0, 0, 0
    for letter in string:
        if letter in LOWERCASE:
            lower_count += 1
        elif letter in UPPERCASE:
            upper_count += 1
        else:
            neither_count += 1
    
    lower_percent = (lower_count / len(string)) * 100
    upper_percent = (upper_count / len(string)) * 100
    neither_percent = (neither_count / len(string)) * 100

    result["lowercase"] = "{:.2f}".format(lower_percent)
    result["uppercase"] = "{:.2f}".format(upper_percent)
    result["neither"] = "{:.2f}".format(neither_percent)

    return result
```