# List of Digits    
## Problem
Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

### Notes
- Split up the digits within a numbe
- Will need to use strings to split them

## Example
```python
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
```

## Data
Data handled is list, integers, and strings.

**Input: Integer**
**Intermediate Steps: String**
**Output: List**

## Algorithm
1. Initialize an empty list
2. Convert integer to a string
3. If the length of the string is 1:
    - Return itself
4. Iterate through the string:
    - Append it to the empty list
5. Return empty list

## Code
```python
def digit_list(number):
    blank = []
    str_number = str(number)
    if len(str_number) == 1:
        blank.append(int(str_number))
    else:
        for digit in str_number:
            blank.append(int(digit))
    return(blank)
```