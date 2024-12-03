# Is It Prime?
## Problem
A prime number is a positive number that is evenly divisible by itself and 1. Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is not a prime since it has divisors of 1,2,3,4,6,8,12,and 24. Note that the number 1 is not prime.

Write a function that takes a positive integers as an argument an returns `true` if the number is prime, `false` if it is not prime.

You may not use any of Python's add-on packages to solve this problem. Your task is to programmatically determine whether a number is prime without relying on functions that already do that for you.

## Example
```python
z
```

## Data
Data handled is integer and boolean.

**Input**: Integer
**Output**: Boolean

## Algorithm
1. Check if number is 1:
    - return false
2. For number between 2 and itself:
    - Check if number is divisible by any of the numbers:
        - Return false
3. Return true

```python
def is_prime(number):
    if number == 1:
        return False
    
    for count in range(2, number):
        if number % count == 0:
            return False
        
    return True
```