# Alphabetical Numbers
## Problem
Write a function that takes a list of integers between `0` and `19` and and returns a list of those integers sorted based on the English word for each number.

## Example
```python
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True
```

## Data
Data handled is simply lists.

**Input**: List
**Output**: List

## Algorithm
1. Initialize constant of alphabetic Numbers
2. Sort the list in alphabetical order
    - apply function to each item
3. Return the sorted list

## Code
```python
NUMBER_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                'twelve', 'thirteen', 'fourteen', 'fifteen',
                'sixteen', 'seventeen', 'eighteen', 'nineteen']

def word_for_number(num):
    return NUMBER_WORDS[num]

def alphabetic_number_sort(numbers):
    return sorted(numbers, key=word_for_number)
```