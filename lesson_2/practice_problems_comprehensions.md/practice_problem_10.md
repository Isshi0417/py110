## Practice Problem 10
## Problem
Write a function that takes no arguments and returns a string that contains a UUID.

## Solution
```python
def generate_uuid():
    alpha = "012345789abcdef"
    sections = [8, 4, 4, 4, 12]
    uuid = []

    for section in sections:
        characters = [random.choice(alpha) for _ in range(sections)]
        uuid.append("".join(characters))

    return "-".join(uuid)
```