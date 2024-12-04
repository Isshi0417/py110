# Binary Search
## Problem
Implement a `binary_search` function that takes a list and search item as arguments, and returns the index of the search item if found, or -1 otherwise. You may assume that the list argument will always be sorted.

## Example
```python
# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)
```

## Data
Data handled are lists.

**Input**: List
**Output**: List

## Algorithm
1. Find the midpoint
2. If the middle value is equal to the search:
    - Return index
3. If the middle value is less than the search:
    - discard lower half including the middle value
    - repeat the process from the top
4. if the middle value is greater than search:
    - discard the upper half including the middle value
    - repeat the process from the top

## Code
```python
def binary_search(lst, search):
    end = len(lst) - 1
    start = 0

    while start <= end:
        mid = start + (end - start) // 2
        if lst[mid] == search:
            return mid
        elif lst[mid] < search:
            start = mid + 1
        else:
            end = mid - 1

    return -1
```
