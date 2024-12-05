# Practice Problem 5
Given the following data structure, sort the list so that the sub-lists are ordered based on the sum of the *odd* numbers that they contain. You shouldn't mutate the original list.

```python
lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
```

## Solution
```python
def odd_sum(numbers):
    odds = [number for number in numbers if number % 2 != 0]
    return sum(odds)

sorted_list = sorted(lst, key=odd_sum)
print(sorted_list)
```