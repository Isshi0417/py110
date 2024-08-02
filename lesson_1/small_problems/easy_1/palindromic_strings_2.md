# Palindromic Strings (Part 2)
## Problem
Write another function that returns `True` if the string passed as a palindrome, or `False` otherwise. This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the `is_palindrome` function you wrote in the previous exercise.

### Notes
- The behavior should be similar to `is_palindrome` or incorporate it
- Must be case and space insensitive
- Must ignore all non-alphanumeric characters

## Examples
```python
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
```

### Clarifications
- A string is considered a palindrome as long as the word mirrors itself.

## Data
The data handled should be a string.

**Input**: string
**Output**: string

## Algorithm
1. Initialize an empty string.
2. For each character in a given string
	- Check if the character is alphanumeric
	- Add the character to the empty string
3. Check if the string is a palindrome

## Code
```python
def is_palindrome(string):
	return string == string[::-1]

def is_real_palindrome(string):
	empty = ''
	for character in string:
		if character.isalnum():
			empty += character.lower()
	return is_palindrome(empty)
```