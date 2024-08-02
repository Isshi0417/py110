# Running Totals
## Problem
Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

### Notes
- Each subsequent number should be additive of the previous number

### Questions
- Do other number types (not int) have to be supported?
- Does it need error handling for non-numeric values?
- Can the given list be empty?

## Example
```python
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
```

### Clarification
- Only integers are handled
- Lists of different lengths need to be supported
- List can be empty
- No data validation needed

## Data
The data handled should be lists and integers. Lists will be used to iterate through the given list and make a new list with added digits.

**Input**: list
**Output**: list

## Algorithm
1. Initialize an empty list
2. Initialize the sum
3. Iterate though the given list
4. For each subsequent number in the list
	- Add to sum
	- Append sum to the empty list
5. Return the list

## Code
```python
def running_total(num_list):
	empty = []
	sum = 0
	for number in num_list:
		sum += number
		empty.append(sum)
	return empty
```
