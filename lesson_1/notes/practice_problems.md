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
*Determine the minimum age from the above `ages` dictionary.*

```python
print(min(ages.values()))
```

## Practice Problem 7
*What would the following code output? Try to answer without running the code.*

```python
words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
	if len(word) > 3:
		selected_words.append(word)

print(selected_words)
```

The code should output `['bear']` because the `if` statement filters out any elements that are 3 letters or less.

## Practice Problem 8
*Given the following string, create a dictionary that represents the frequency with each letter occurs. The frequency count should be case-sensitive:*

```python
statement = "The Flintstones Rock"
broken_down = {}

for char in statement:
	if char == ' ':
		continue
	elif char not in broken_down:
		broken_down[char] = 1
	else:
		broken_down[char] += 1
print(broken_down)
```

## Practice Problem 9
*What is the return value of the list comprehension below? Try to answer without running the code.*

```python
[num for num in [1, 2, 3] if num > 1]
```

This should return `[2, 3]`.  It filters any numbers greater than `1` and returns the list.

## Practice Problem 10
*What does the following code print and why?*

```python
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())
```

It should output `{'b': 'bear'}` since `popitem()` removes the last entry from the dictionary and returns it, which means the dictionary will only have `{'a': 'ant'}`, but the popped item is `{'b': 'bear'}`.

## Practice Problem 11
*What does the following code return? Try to answer without running the code.*

```python
lst = [1, 2, 3, 4, 5]
lst[:2]
```

It should return `[1, 2]`. When using indexes, the numbers within the index represent `[start:end:step]`, where `step` is optional. In this case, the returned value starts at the beginning of the list and ends when the index value is `2`. It's important to note that like `range()`, the ending value is not inclusive.

## Practice Problem 12
*What would be the output of the code below: Try to answer without running the code.*

```python
frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)
```

The code will output an error because frozen sets are immutable in Python. This means `add()` is not a valid built-in function to manage frozen sets.
