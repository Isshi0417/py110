# Fibonacci Numbers (Memoization)
## Problem
Refactor the recursive function to use memoization

## Example
![fibonacci table with memoization of calculated numbers](image.png)

## Data
Data handled are dictionary and integer.

**Input**: Integer
**Intermediate Step**: Dictionary
**Output**: Integer

## Algorithm
1. Initialize empty dictionary
2. If number is less than or equal to 2:
    - return 1
3. elif number is in dictionary:
    - return memo[number]
4. else:
    - add to dictionary
    - return memo[number]

## Code
```python
def fibonacci(number):
    computed = {}

    if number <= 2:
        return 1
    elif number in computed:
        return computed[number]
    else:
        computed[number] = fibonacci(number - 1) + fibonacci(number - 2)
        return computed[number]
```