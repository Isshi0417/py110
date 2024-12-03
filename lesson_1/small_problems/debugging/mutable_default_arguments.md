# Mutable Default Arguments
## Problem
We want to create a function that appends a given value to a list. However, the function seems to be behaving unexpectedly:

```python
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
```

How would you fix this code?

## Answer
The issue is that the list is not reset every time the function is executed. To fix this, the list can be initialized within the function.

```python
def append_to_list(value):
    lst = []
    lst.append(value)
    return lst
```