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

## Computer AI: Defense
```python
def find_at_risk_square(line, board):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count('X') == 2:
        for square in line:
            if board[square] == ' ':
                return square
    return None
```