# Practice Problem 4
## Problem
How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?

```python
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]
```

## Solution
```python
def published_year(entry):
    return int(entry["published"])

print(sorted(books, key=published_year))
```