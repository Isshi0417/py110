# Rotation (Part 3)
## Problem
Take the number `735191` and rotate it by one digit to the left, getting `352917`. Next, keep the first digit fixed in place and rotate the remaining digits to get `329175`. Keep the first two digits fixed in place and rotate again to get `321759`. Keep the first three digits fixed in place and rotate again to get `321597`. Finally, keep the first four digits fixed in place and rotate the final two digits to get `321579`. The resulting nubmer is called the `maximum rotation` of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the `rotate_right_most_digits` function from the previous exercise.

## Example
```python
print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True
```

## Data
Data handled is integer and string.

**Input**: Integer
**Intermediate Steps**: String
**Output**: String

## Algorithm
1. Convert the integer to a string
2. Iterate through the length of the string in inverse order:
    - rotate the right most digits starting from the specific slice
3. Convert the string to integer
4. Return the result

```python
def max_rotation(number):
    for count in range(len(str(number)), 1, -1):
        number = rotate_rightmost_digits(number, count)
    return number
```