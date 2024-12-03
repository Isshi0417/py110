# Key Check
## Problem
You have a function that should check whether a key exists in a dictionary and returns its value. However, it's raising an error. Why is that? How would you fix this code?

```python
def get_key_value(my_dict, key):
    if my_dict[key]:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))
```

## Answer
The program raises an error because there is no such key "b" in the given dictionary. This can be fixed by using get() by passing a default value (`None`).

```python
def get_key_value(my_dict, key):
    return my_dict.get(key, None)
```