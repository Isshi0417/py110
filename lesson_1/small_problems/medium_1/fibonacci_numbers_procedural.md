# Fibonacci Numbers (Procedural)
## Problem
The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. The first two Fibonacci numbers are `1` and `1`. The third number is `1 + 1 = 2`, the fourth is `1 + 2 = 3`, the fifth is `2 + 3 = 5`, the sixth is `3 + 5 = 8`, and so on. In mathematical terms, this can be represented as:

```
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)
```

Write a function called `fibonacci` that computes the `nth` Fibonacci number, where `nth` is an argument passed to the function.

## Example

```python
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
```

## Data
Data handled are integers.

**Input**: Integer
**Output**: Integer

## Algorithm
1. Check if number is <= 2:
    - Return 1
2. Initialize sum and set it to 1
3. Initialize number to add and set it to 1
4. For each number within the range of 3 to number + 1:
    - set previous number to current
    - add previous and current number
5. Return the sum

```python
def fibonacci(number):
    if number <= 2:
        return 1
    
    previous = 1
    current = 1

    for _ in range(3, number + 1):
        previous, current = current, previous + current
    
    return current
```