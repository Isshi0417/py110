# Practice Problems

## Practice Problem 1
*Given the tuple:*

```python
fruits = ("apple", "banana", "cherry", "date", "banana")
```

*How would you count the number of occurrences of "banana" in the tuple?*

```python
print(fruits.count("banana"))
```

## Practice Problem 2
Consider the set:

```python
numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers))
```

*What is the set's length? Try to answer without running code.*

The set's length should be `5`. Since sets can't contain duplicate values, it will automatically ignore any repeating values. This means it only counts each number once.