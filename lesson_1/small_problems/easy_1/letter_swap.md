# Letter Swap
## Problem
Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

### Notes
- Only the first and the last letters are manipulated (rest stays the same)

### Questions
- Do the swapped letters retain its case?

## Example
```python
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
```

### Clarifications
- Letters retain their case even after swapped

## Data
Data handled should be strings and list.

**Input**: string
**Output**: string

## Algorithm
1. Split up the string into a list of words
2. Initialize an empty list
3. Check if the length of the string is 1 character long
	- Append to the empty list
4.  For each word in the list
	- Swap the first and last character
	- Transform the word
	- Append to the empty list
5. Join the empty list with a space
6. Return the joint string

## Code
```python
def swap(string):
	words = string.split()
	result = []

	for word in words:
		if len(word) == 1:
			result.append(word)
		else:
			first = word[0]
			last = word[-1]
			word = last + word[1:-1] + first
			result.append(word)

	return " ".join(result)
```