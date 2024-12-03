# Fibonacci Number Location By Length
## Problem
Write a function that calculates and returns the index of the fist Fibonacci number that has the number of digits, specified by the argument. The first Fibonacci number has an index of 1. You may assume that the argument is always an integer greater than or equal to 2.

## Example
```python
# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)
```

## Data
Data handled is integers.

**Input**: Integer
**Output**: Integer

## Algorithm
1. import sys
2. set the max digits to 50_000
3. set the first and second fibonacci numbers to 1
4. set count to 2
5. while length of the second number is less than the given number:
    - do fibonacci
    - increase index by 1
6. Return the count

## Code
```python
import sys

sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(number):
    previous = 1
    current = 1
    count = 2

    while len(str(current)) < number:
        previous, current = current, previous + current
        count += 1

    return count
```