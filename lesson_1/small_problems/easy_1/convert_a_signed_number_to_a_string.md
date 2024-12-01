# Convert a Signed Number to a String
## Problem
In the previous exercise, you developed a function that converts non-negative numbers to strings. In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string representation.

You may not use any of the standard conversion functions available in Python, such as `str`. You may, however, use `integer_to_string` from the previous exercise.

### Notes
- Integers must be converted to strings

### Questions
- Do positive numbers need a positive sign at the front?
- Can the number be negative?

## Example
```python
print(signed_integer_to_string(4321) == "+4321")    # True
print(signed_integer_to_string(-123) == "-123")     # True
print(signed_integer_to_string(0) == "0")           # True
```

### Clarifications
- Positive numbers need a positive sign
- Negative numbers also need to be accounted for

## Data
Data handled are strictly integers and strings.

**Input: Integer**
**Output: String**

## Algorithm
1. Initialize digits list that hold the strings
2. Initialize an empty string
3. Check:
    - If number is less than 0:
        - Return "-" + integers_to_string(-number)
    - Elif number is greater than 0:
        - Return "+" + integers_to_string(number)
    - Else:
        - Return "0"

## Code
```python
def signed_integer_to_string(number):
    if number < 0:
        return f"-{integer_to_string(-number)}"
    elif number > 0:
        return f"+{integer_to_string(number)}"
    else:
        return 0

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
