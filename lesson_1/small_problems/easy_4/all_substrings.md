# All Substrings
## Problem
Write a function that returns a list of all substrings of a string. Order the returned list by where in the string the substring begins. This means that all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on. Since multiple substrings will occur at each positio, return the substrings at a given index shortest to longest.

You may (and should) use the `leading_substrings` function you wrote in the previous exercise.

## Example
```python
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
```

## Data
Data handled are string and list.

**Input**: String
**Output**: List

## Algorithm
1. Initialize empty list
2. Iterate through the length of the string:
    - Initialize the starting string
    - Iterate through the substring:
        - Append substring to the list
3. Return the list

## Code
```python
def leading_substrings(string):
    item = ""
    result = []
    for letter in string:
        item += letter
        result.append(item)
    return result

def substrings(string):
    result = []
    for index in range(len(string)):
        letter = string[index:]
        for substring in leading_substrings(letter):
            result.append(substring)
    return result
```