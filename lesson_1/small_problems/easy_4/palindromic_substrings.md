# Palindromic Substrings
## Problem
Write a function that returns a list of a ll palindromic substrings of a string. That is, each substring must consist of a sequence of characters that reads the same forward and backward. The substrings in the returned list should be sorted by their order of appearance in the input string. Duplicate substrings should be included multiple times.

You may (and should use) `substrings` function you wrote in the previous exercise.

For the purpose of this exercise, you should consider all characters and pay attention to case; that is 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, assume that single characters are not palindromes.

## Example
```python
print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True
```

## Data
Data handled is strings and lists.

**Input**: String **Output**: List

## Algorithm
1. Initialize empty list.
2. Check if the inverse of the substring is equal:
    - Add to the list
3. Else:
    - Continue
4. Return the list

## Code
```python
def is_palindrome(word):
    return len(word) > 1 and word == word[::-1]

def palindromes(string):
    result = []
    for substring in substrings(string):
        if is_palindrome(substring):
            result.append(substring)
    return result
```