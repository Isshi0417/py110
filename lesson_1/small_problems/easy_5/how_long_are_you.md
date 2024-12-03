# How Long Are You?
## Problem
Write a function that takes a string as an argument and returns a list that contains every word from the string, with each word followed by a space and the word's length. If the argument is an empty string or if no argument is passed, the function should return an empty list.

You may assume that every pair of words in the string will be separated by a single space.

## Example
```python
# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True
```

## Data
Data handled are strings and lists.

**Input**: String
**Output**: List

## Algorithm
1. Initialize an empty list
2. Copy the word and find the length of the string
3. Concatenate the string
4. Append the concatenated string to the empty list
5. Return the list

## Code
```python
def find_length(string):
    return string + " " + str(len(string))

def word_lengths(words = ""):
    if not words:
        return []

    result = []
    words_lst = words.split(" ")
    for word in words_lst:
        result.append(find_length(word))
    return result
```