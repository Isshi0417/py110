# Merge Sorted Lists
## Problem
Write a function that takes two sorted lists as arguments and returns a new list that contains all the elements from both input lists in ascending sorted order. You may assume that the lists contain either all integer values or all string values.

You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

## Example
```python
# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)
```

## Data
Data handled are lists.

**Input**: List
**Output** List

## Algorithm
1. Initialize an empty list
2. Compare each element in the list:
    - Append the one thats smaller
3. Return the result and the remaining item

## Code
```python
def merge(lst1, lst2):
    first = lst1[:]
    second = lst2[:]
    result = []

    while first and second:
        if first[0] <= second[0]:
            result.append(first.pop(0))
        else:
            result.append(second.pop(0))
    
    return result + first + second
```