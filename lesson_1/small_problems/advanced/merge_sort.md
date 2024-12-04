# Merge Sort
## Problem
Write a function that takes a list argument and returns a new list that contains the values from the input list in sorted order. The function should sort the list using the merge sort algorithm as described above. You may assume that every element of the list will have the same data type: either all numbers or all strings.

Feel free to use the `merge` function you wrote in the previous exercise.

## Example
```python
# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)
```

## Data
Data handled are lists.

**Input**: List
**Output**: List

## Algorithm
1. Initialize an empty list
2. While the sub-list contains more than 1 value:
    - Split into half
3. Merge by sorting it
4. Return the result

## Code
```python
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    sub_list1 = lst[:len(lst) // 2]
    sub_list2 = lst[len(lst) // 2:]

    sub_list1 = merge_sort(sub_list1)
    sub_list2 = merge_sort(sub_list2)

    return merge(sub_list1, sub_list2)
```