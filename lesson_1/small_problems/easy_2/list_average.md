# List Average
## Problem
Write a function that takes one argument, a list of integers, and returns the average of all the integers in the list, rounded down to the integer component of the average. The list will never be empty, and the numbers will alwaysbe positive integers.

### Note
- Should output the average of the sum

### Question
- Do negative numbers need to be accounted for?

## Example
```python
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True
```

### Clarification
- Negative numbers do not need to be accounted for
- Single valuess need to be accounted for

## Data
Data used are explicitly lists and integers.

**Input: List**
**Output: Integer**

## Algorithm
1. Initialize a sum
2. Iterate through the list:
    - Add the value to the sum
3. Divide sum by the length of the list
4. Round down
4. Return average

## Code
```python
def average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return int(sum / len(numbers))
```