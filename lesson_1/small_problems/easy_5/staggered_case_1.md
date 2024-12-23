# Staggered Case (Part 1)
## Problem
Write a function that takes a string as an argument and returns the string with a staggered capitalization scheme. Every other character, starting from the first, should be capitalized and should be followed by a lowercase or non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters for determining when to switch between upper and lower case.

## Example
```python
string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
```

## Data
Data handled are strings.

**Input**: String
**Output**: String

## Algorithm
1. Iterate through string:
    - If the index is odd:
        - Lowercase
    - Else:
        - Uppercase
2. Return the result

```python
def staggered_case(string):
    result = ""
    for i in range(len(string)):
        if (i % 2 == 0):
            result += string[i].upper()
        elif (i % 2 != 0):
            result += string[i].lower()
        else:
            result += string[i]
    return result
```