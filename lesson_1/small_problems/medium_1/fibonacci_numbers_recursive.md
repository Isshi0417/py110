# Fibonacci Numbers (Recursion)
## Problem
Given this recursive algorithm, try to write a recursive function that computes the `nth` Fibonacci number, where `nth` is an argument passed to the function.

## Example
```python
print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True
```

## Data
Data handled is integer.

**Input**: Integer
**Output**: Integer

## Algorithm
1. Check if number is less than or equal to 2:
    - return 1
2. Return the sum of previous and current number

```python
def fibonacci(number):
    if number <= 2:
        return 1
    
    return fibonacci(number - 1) + fibonacci(number - 2)
```
