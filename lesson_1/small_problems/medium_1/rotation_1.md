# Rotation (Part 1)
## Problem
Write a function that rotates a list by moving the first element to the end of the list. Do not modify the original list; return a new list instead.

- If the input is an empty list, return an empty list.
- if the input is not a list, return None.

Review the test cases below, then implement the solution accordingly.

### Notes
- The first element goes to the end, and the rest of the items slide one to the left.

## Example
```python
# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])
```

## Data
Data handled are simply lists.

**Input**: List
**Output**: List

## Algorithm
1. Check if the argument is not a list:
    - Return None
2. Check if the list is empty:
    - Return empty list
3. Copy the list.
4. Pop the first element and append it to the end.
5. Return the copy  

```python
def rotate_list(lst = []):
    if not isinstance(lst, list):
        return None
    
    if len(lst) == 0:
        return []

    lst_copy = lst.copy()
    first = lst_copy.pop(0)
    lst_copy.append(first)

    return lst_copy
```