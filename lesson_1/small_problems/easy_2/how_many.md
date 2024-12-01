# How Many?
## Problem
Write a function that counts the number of occurences of each element in a given list. Once counted, print each element alongside the number of occurences. Consider the words case sensitive e.g. ("suv" != "SUV").

### Notes
- Words are case sensitive
- Dictionaries should be used to keep count of the words in the list.

## Example
```python
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
```

```shell
# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2
```

## Data
Data used is strictly list and dictionary.

**Input: List**
**Output: Formatted Dictionary**

## Algorithm
1. Initialize empty dictionary
2. Iterate through each item in the list:
    - If the item exists:
        - Add increase the key by 1
    - Else:
        - Set the frequency to 1
3. Print the output

## Code
```python
def count_occurrences(words):
    frequency = {}
    for item in words:
        if (item in frequency):
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    for key, value in frequency.items():
        print("%s => %d" % (key, value))
```