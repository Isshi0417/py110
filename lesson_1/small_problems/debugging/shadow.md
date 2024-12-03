# Shadow
## Problem
We defined a function intending to multiply the sum of numbers by a factor. However, the function raises an error. Why? How would you fix this code?

```python
def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)
```

## Answer
The built-in function `sum()` is shadowed by the currently declared function. This means that the function is being called recursively when finding the sum. The name of the function can be changed to fix this issue.

```python
def sum_factors(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_factors(numbers, 2) == 20)
```