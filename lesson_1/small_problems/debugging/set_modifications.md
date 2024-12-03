# Set Modifications
## Problem
We want to remove certain items from a set while iterating over it, but the code below throws an error. Why is that and how can we fix it?

```python
data_set = {1, 2, 3, 4, 5}

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)
```

## Answer
The size of a set can't be changed while iterating over it. The same can be achieved by using set comprehensions to build a new set by iterating over the original and applying a new condition.

```python
result = set()

for item in data_set:
    if item % 2 != 0:
        result.add(item)
return result
```