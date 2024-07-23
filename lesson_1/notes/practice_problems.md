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
*Consider the set:*

```python
numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers))
```

*What is the set's length? Try to answer without running code.*

The set's length should be `5`. Since sets can't contain duplicate values, it will automatically ignore any repeating values. This means it only counts each number once.

## Practice Problem 3
*Given two sets:*

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

*How would you obtain a set that contains all the unique values from both sets?*

```python
print(a.union(b))
```

## Practice Problem 4
*Given the following code, what would the output be? Try to answer without running the code.*

```python
names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
	name_positions[name] = index
print(name_positions)
```

The code should print a dictionary that follows the format `{"Name": "Position"}` for each element in the list.

## Practice Problem 5
*Calculate the total age given the following dictionary:*

```python
ages = {
	"Herman": 32,
	"Lily": 30,
	"Grandpa": 5843,
	"Eddie": 10,
	"Marilyn": 22,
	"Spot": 237,
}
total = 0
for name in ages:
	total += ages[name]

print(total)
```

## Practice Problem 6
Determine the minimum age from the above `ages` dictionary.

```python
print(min(ages.values()))
```

