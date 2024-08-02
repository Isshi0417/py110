# Letter Counter (Part 1)
## Problem
Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

### Notes
- Count the number of letters in a word and store its data in a dictionary
- Spaces are not counted
- Case shouldn't matter

### Questions
- Can the given string be empty?
- Is data validation required? (check if not string)

## Example
```python
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
```

### Clarifications
- Given string can be empty
- No data validation needed

## Data
The data handled should be strings and dictionaries.

**Input**: String
**Output**: Dictionary

## Algorithm
1. Split the string into a list by the surrounded symbol
2. Initialize an empty dictionary
3. For each word in the list
	- Check if the length (key) already exists
		- Count the number of characters in the word
		- Add the number of characters as a key to the dictionary
	- If it exists already
		- Increment the value of the given length (key)
4. Return the dictionary

## Code
```python
def word_sizes(sentence):
	empty = {}
	words = string.split()

	for word in words:
		if len(word) not in empty:
			empty[len(word)] = 1
		else:
			empty[len(word)] += 1

	return empty
```