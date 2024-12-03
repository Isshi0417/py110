# Reverse a String
## Problem
You have a function that is supported to reverse a string passed as an argument. However, it's not producing the expected output. Explain the bug, and provide a solution.

```python
def reverse_string(string):
    for char in string:
        string = char + string

    return string

print(reverse_string("hello") == "olleh")
```

## Answer
The code makes it so that the original string is concatenated at the end. This makes the value `ollehhello`. This can be fixed by reassigning string to its inverse using the slice function such that `string = string[::-1]`.