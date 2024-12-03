# Copy Issues
## Problem
We have a list of lists and want to duplicate it. After making the copy, we modify hte original list, but the copied list also seems to be affected:

```python
import copy

original = [[1], [2], [3]]
copied = copy.copy(original)

original[0][0] = 99

print(copied[0] == [1])
```

What's wrong here? How can you fix it?

## Answer
When using `copy()`, Python makes a shallow copy instance of the original list. This means that any changes made to the original will also mutate the copied list. One way to fix this is to create a deep copy that does not share an object instance with the original list.

```python
import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])
```