# Next Featured Number Higher than a Given Value
## Problem
A *featured number* is an odd number that is a multiple of 7, with all of its digits occurring exactly once each. For example, `49` is a featured number, but `98` is not odd (it is not odd), `97` is not (it is not a multiple of 7), and `133` is not (the digit 3 appears twice.)

Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

## Example
```python
print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
```

## Data
Data handled is integer.

**Input**: Integer
**Output**: Integer

## Algorithm
1. If the number is greater than 9876543201:
    - Return "There is no possible number that fulfills those requirements.
2. Convert the number into string:
    - Check for unique values:
        - If there are repeating values:
            - Return False
    - Return True
3. Check if number is odd and divisible by 7 and unique and greater than the original number:
    - Return the number

## Code
```python
def is_unique(number):
    number_str = str(number)
    digits = []

    for digit in number_str:
        if digit not in digits:
            digits.append(digit)
        else:
            return False
    
    return True

def next_featured(number):
    featured = 0

    if number >= 9876543201:
        return "There is no possible number that fulfills those requirements."
    
    while (featured <= number) or (featured % 2 == 0) or (featured % 7 != 0) or (not is_unique(featured)):
        featured += 1

    return featured
```