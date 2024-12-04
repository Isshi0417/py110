# Triangle Sides
## Problem
Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four string representing the triangle's classification: `equilateral`, `isosceles`, `scalene`, or `invalid`.

## Example
```python
print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
```

## Data
Data handled is integers and strings.

**Input**: Integer
**Output**: String

## Algorithm
1. Check if the two shortest side are shorter than the longest length:
    - return invalid
2. If all three sides are equal:
    - return equilateral
3. Elif all three sides are not equal:
    - return scalene
4. Else:
    - return isosceles

```python
def triangle(side1, side2, side3):
    perimeter = side1 + side2 + side3
    longest = max(side1, side2, side3)
    shortest = min(side1, side2, side3)
    middle = perimeter - longest - shortest

    if shortest + middle <= longest:
        return "invalid"
    
    if shortest == middle == longest:
        return "equilateral"
    elif shortest == middle or longest == middle:
        return "isosceles"
    else:
        return "scalene"
```