# Reverse Number
## Problem
Write a function that takes a positive integer as an argument and 
returns that number with its digits reversed.

## Example
```python
print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True
```

## Data
Data handled are integers and strings.

**Input**: Integer
**Intermediate Step**: String
**Output**: Integer

## Algorithm
1. Convert integer to string
2. Reverse string
3. Convert string to integer
4. Return the integer

## Code
```python
def reverse_number(number):
    number_str = str(number)
    return int(number_str[::-1])
```