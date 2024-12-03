# Staggered Case (Part 2)
## Problem
Modify the function from the pervious exercise so it ignores non-alphabetic characters when determining whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.

## Example
```python
string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
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
1. Initialize empty string
2. Iterate through the string:
    - Check if the character is alphabetical
    - Alternate casing
    - Else:
        - Add the character to the result
3. Return the result

## Code
```python
def staggered_case(string):
    result = ''
    upper = True

    for char in string:
        if char.isalpha():
            if upper:
                result += char.upper()
            else:
                result += char.lower()
            upper = not upper
        else:
            result += char

    return result
```