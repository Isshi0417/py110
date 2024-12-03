# List Deduplication
## Problem
A developer is trying to remove duplicates from a list. They use a set for deduplication, but the order of elements is lost. How can we preserve the order?

```python
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed
```

## Answer
In order to preserve the order, list must be used. Similar effect can be achieved by checking whether the item is `in` the new list or not.

```python
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]

def unique_data(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(unique_data(data) == [4, 2, 1, 3])
```
