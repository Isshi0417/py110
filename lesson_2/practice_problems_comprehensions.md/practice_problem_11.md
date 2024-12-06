# Practice Problem 11
## Problem
The following dictionary has list values that contain strings. Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.

```python
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
```

## Solution
```python
VOWELS = "aeiou"

list_of_vowels = []
for key in dict1:
    for word in dict1[key]:
        for letter in word:
            if letter in VOWELS:
                list_of_vowels.append(letter)

list_of_vowels = [letter for key in dict1
                         for word in dict1[key]
                         for letter in word if letter in VOWELS]
```
