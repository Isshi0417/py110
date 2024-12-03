# Multiply List
## Problem
You want to multiply all elements of a list by 2. However, the function is not returning the expected result. Explain the bug, and provide a solution.

```python
def multiply_list(lst):
    for item in lst:
        item *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])
```

## Answer
The issue is that the multiplied items are not appended to a separate list.
This means the an empty list must be initialized and the multiplied items 
should be appended to the empty list.

```python
def multiply_list(lst):
    result = []
    for item in lst:
        result.append(item * 2)

    return result
```