# Combine Two Lists
## Problem
Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both list arguments, with each element taken in alternation.

You may assume that both input lists are non-empty, and that they have the same number of elements.

### Notes
- Combine two lists and return a anew list that contains all elements, alternting.

## Example
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True
```

## Data
Data type handled is stricly lists.

**Input: List**
**Output: List**

## Algorithm
1. Initalize an empty list
2. Set the number of iteration to the length of the list
3. Iterate through the length of each list:
    - Add item from each list to the empty list
4. Return empty list

## Code
```python
def interleave(list1, list2):
    blank = []
    number = len(list1)

    for i in range(number):
        blank.append(list1[i])
        blank.append(list2[i])
    
    return blank
```