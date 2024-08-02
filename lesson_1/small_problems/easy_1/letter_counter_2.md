# Letter Counter (Part 2)
## Problem
Modify the `word_sizes` function from the previous exercise to exclude non-letters when determining word size. For instance, the word size of `"it's"` is `3`, not `4`.

### Notes
- No punctuation should be counted

### Questions
- Is data validation needed?
- Can a string be empty?

## Example
```python
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})
```

### Clarifications
- The same assumptions hold still as the previous assignment

## Data
The data handled should still be the exact same:  string and dictionary.

## Algorithm
1. Split the string into a list by spaces
2. Initialize an empty dictionary
3. For each word in the list
	- Remove any non-alphanumeric values
	- Count the length of the word
4. Check if the length (key) already exists
	- Add the number of characters as a key to the dictionary
5. If it already exists
	- Increment the value of the given length (key)
6. Return the dictionary

## Code
```python
def word_sizes(string):
	empty = {}
	words = string.split()

	for word in words:
		for character in word:
			if not character.isalnum():
				word = word.replace(character, "")

		if len(word) not in empty:
			empty[len(word)] = 1
		else:
			empty[len(word)] += 1

	return empty
```
