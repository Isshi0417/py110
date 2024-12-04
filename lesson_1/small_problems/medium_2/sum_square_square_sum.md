# Sum Square - Square Sum
## Problem
Write a function that computes the difference between the square of the sum of the first `count` positive integers and the sum of the squares of the fist `count` positive integers.

## Example
```python
print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True
```

## Data
Data handled is integer.

**Input**: Integer
**Output**: Output

## Algorithm
1. Find sum square
2. Find square sum
3. Find the difference

## Code
```python
def sum_square(number):
    sum = 0
    for value in range(1, number + 1):
        sum += value
    return sum ** 2

def square_sum(number):
    sum = 0
    for value in range(1, number + 1):
        sum += (value ** 2)
    return sum

def sum_square_difference(number):
    return sum_square(number) - square_sum(number)
```