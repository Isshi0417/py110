# Matching Parenthesis?
## Problem
Write a function that takes a string a an argument and returns `True` if all parentheses in the string are properly balanced, `False` otherwise. To be properly balanced, parentheses must occur in matching `(` and `)` pairs.

## Example
```python
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
```

## Data
Data handled is strictly strings.

**Input**: String
**Output**: String

## Algorithm
1. Set count to 0
2. If character is (:
    add one
3. If character is ):
    subtract one
4. If count is negative, return false
5. Return if count is 0

## Code
```python
def is_balanced(string):
    count = 0
    for character in string:
        if character == "(":
            count += 1
        elif character == ")":
            count -= 1
        if count < 0:
            return False
    
    return count == 0
```