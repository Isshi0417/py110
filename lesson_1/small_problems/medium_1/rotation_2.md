# Rotation (Part 2)
## Problem
Write a function that rotates the last `count` digits of a `number`. To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

## Example
```python
print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
```

## Data
Data handled is integers and strings.

**Input**: Integer
**Intermediate Steps**: String
**Output**: Integer

## Algorithm
1. Convert the number to a string
2. Split the string into two halves based on the number
3. Rotate the number
4. Convert it back to integer
5. Return the result

```python
def rotate_string(string):
    return string[1:] + string[0]

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_half = number_str[:-count]
    second_half = number_str[-count:]
    result_str = first_half + rotate_string(second_half)

    return int(result_str)
```