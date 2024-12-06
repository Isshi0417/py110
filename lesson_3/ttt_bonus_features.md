# Assignment: TTT Bonus Features
## Improved Join
```python
def join_or(lst, separator = ", ", conjunction = "or"):
    if lst == []:
        return ""
    elif len(lst) == 1:
        return lst[0]

    lst_str = [str(number) for number in lst]
    first = separator.join(lst_str[0:-1])
    return f"{first} {conjunction} {lst_str[-1]}"
```