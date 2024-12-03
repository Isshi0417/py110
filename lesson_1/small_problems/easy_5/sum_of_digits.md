# Sum of Digits
## Problem
Write a function that takes one argument, a positive integer, and returns the sum of its digits.

## Example
```python
print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True
```

## Data
Data handled are strings and integers.

**Input**: Integer
**Intermediate Steps**: String
**output**: Integer

## Algorithm
1. Initialize sum
2. Convert integer to string
3. Iterate through the string:
    - Add the digit to the sum
4. Return the sum

## Code
```python
def sum_digits(number):
    sum = 0
    number_str = str(number)
    for digit in number_str:
        sum += int(digit)
    return sum
```