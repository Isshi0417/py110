# Convert a Number to a String
## Problem
In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. In this exercise and the next, you're going to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

You may not use any of the standard conversion functions available in Python, such as `str`. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

### Notes
- Integers must be turned into a string

### Questions
- Is data validation needed?
- Can the number be negative?

## Example
```python
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
```

### Clarifications
- No data validation needed
- Only positive numbers
- The number can be 0

## Data
Data handled are strictly integers and strings.

**Input**: integer
**Output**: string

## Algorithm
1. Initialize digits list that hold the strings
2. Initialize an empty string
3. Check if the number is greater than 0
	- If greater than 0
		- Loop while the number is greater than 0
		- Divide the number by 10
		- Add the remainder to the beginning of the result string
	- If not
		- Return "0"
4. Return result

## Code
```python
def integers_to_string(number):
	DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	result = ""

	if number > 0:
		while number > 0:
			number, remainder = divmod(number, 10)
			result = DIGITS[remainder] + result
	else:
		return "0"

	return result
```