# Name Swapping
## Problem
Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.

## Example
```python
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
```

## Data
Data handled is strings and lists.

**Input**: String
**Intermediate Step**: List
**Output**: String

## Algorithm
1. Split the string into a list
2. Join the list
3. Return the joined string

## Code
```python
def swap_name(name):
    inverted = name.split(" ")[::-1]
    return ", ".join(inverted)
```