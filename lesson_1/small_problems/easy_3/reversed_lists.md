# Reversed Lists
## Problem
Write a function that takes a list as an argument and reverses its elements, in place. That is, mutate the list passed into the function. The returned object should be the same object used as the argument.

You may not use the `list.reverse` method nor may you use a slice ([::-1]).

## Example
list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True

## Data
Data handled is explicitly a list.

**Input**: List
**Output**: List

## Algorithm
1. While start is less than end:
    - swap elements at start and end
    - move the start index forward
    - move the end index backward
2. Return the list

## Code
```python
def reverse_list(lst):
    start, end = 0, len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst
```