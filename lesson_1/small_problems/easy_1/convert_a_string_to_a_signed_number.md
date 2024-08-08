# Convert a String to a Signed Number
## Problem
In the previous exercise, you developed a function that converts simple numeric strings to integers. In this exercise, you're going to extend that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number as an integer. The string may have a leading `+` or `-` sign; if the first character is a `+`, your function should return a positive number; if it is a `-`, your function should return a negative number. If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, such as `int`. You may, however, use the `sting_to_integer` function from the previous exercise.

### Notes
- Should behave the same way as previous assignment
- Must be sign sensitive

### Questions
- Do we need data validation?

## Example
```python
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
```

### Clarifications
- No data validation needed

## Data
Data handled should be dictionary (for the numbers) and integer (for the output).

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
5. If there is a negative sign in the string
	- Make it negative
6. Return sum

## Code
```python
def string_to_integer(string):
	DIGITS = {
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

	value = 0
	for character in string:
		value = (10 * value) + DIGITS[character]

	return value

def sign(string):
	if "-" in string:
		return -string_to_integer(string[1:])
	elif "+" in string:
		return string_to_integer(string[1:])
	else:
		return string_to_integer(string)
```