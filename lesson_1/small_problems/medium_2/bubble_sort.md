# Bubble Sort
## Problem
Write a function that takes a list as an argument and sorts that list using the bubble sort algorithm described above. The sorting should be done "in-place" -- that is, the function should mutate the list. You may assume that the list contains at least two elements.

## Example
```python
lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True
```

## Data
Data handled is a lit.

**Input**: List
**Output**: List

## Algorithm
1. Set sorted to False
2. While sorted is False:
    - Iterate through the list:
        - If the next value is less than current value:
            - Swap
        - If the next value is greater all the way:
            - Set sorted to True
3. Return the result

```python
def bubble_sort(lst):
    while True:
        swapped = False
        for index in range(1, len(lst)):
            if lst[index - 1] <= lst[index]:
                continue

            lst[index - 1], lst[index] = lst[index], lst[index - 1]
            swapped = True
        
        if not swapped:
            break
```