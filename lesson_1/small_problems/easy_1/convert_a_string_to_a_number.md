# Convert a String to a Number
## Problem
Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as `int`. Your function should calculate the result by using the characters in the string.

For now, do not worry about leading `+` or `-` signs, nor should you worry about invalid characters; assume all characters are numeric.

### Notes
- No data validation needed
- Each digit must add up to the integer value

## Example
```python
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
```

## Data
Data handled are strictly strings and integers.

**Input**: string
**Output**: integer

## Algorithm
1. Initialize digits dictionary
2. Initialize sum
3. Initialize place
4. For each character in the string
	- number * 10^n
	- add to sum
	- increment place
5. Return sum

## Code
```python
def string_to_integer(string):
	digits = {
		"0" : 0,
		"1" : 1,
		"2" : 2,
		"3" : 3,
		"4" : 4,
		"5" : 5,
		"6" : 6,
		"7" : 7,
		"8" : 8,
		"9" : 9,
	}

	total = 0
	place = 0

	for i in range(len(string) - 1, -1, -1):
		total += digits.get(string[place]) * 10**i
		place += 1

	return total
```