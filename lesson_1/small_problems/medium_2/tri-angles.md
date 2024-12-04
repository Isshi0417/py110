# Tri-Angles
## Problem
Write a function that takes the three angles ofa triangle as arguments and returns one of the following four strings  repeating the triangle's classification: `right`, `acute`, `obtuse`, or `invalid`.

## Example
```python
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
```

## Data
Data handled are integer and string.

**Input**: Integer
**Output**: String

## Algorithm
1. Initialize a list of angles
2. If 0 is in the list or angles don't total 180:
    - Return invalid
3. If 90 is in the list:
    - Return right
4. Elif all angles are less than 90:
    - Return acute
5. Else:
    - Return obtuse

```python
def triangle(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]

    if (0 in angles) or (angle1 + angle2 + angle3) != 180:
        return "invalid"
    
    if 90 in angles:
        return "right"
    elif (angle1 < 90) and (angle2 < 90) and (angle3 < 90):
        return "acute"
    else:
        return "obtuse"
```