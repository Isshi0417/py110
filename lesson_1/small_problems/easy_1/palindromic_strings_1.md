# Palindromic Strings (Part 1)

## Problem
Write a function that returns `True` if the string is passed as an argument is a palindrome, `False` otherwise. A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.`

### Notes
- Function should return `True` if the given string is a palindrome
- Return false if not a palindrome
- Case insensitive

### Question
- Would it still be considered a palindrome if there was a space between the characters

## Example
```python
# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
```

### Clarifications
- Cases matter and spaces also matter
	- Palindromes need to be exact mirrors

## Data
The data handled should be strings. The function should take one argument.

Input: string
Output: boolean

## Algorithm
1. Check if string and its reversed version are equal

## Code
```python
def is_palindrome(string):
	return string == string[::-1]
```