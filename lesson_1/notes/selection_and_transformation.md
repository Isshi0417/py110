# Selection and Transformation

## Using Loops
```python
numbers = [1, 3, 9, 11, 1, 4, 1]
ones = []

for current_num in numbers:
	if current_num == 1:
		ones.append(current_num)

print(ones)
```

`if` condition determines which values are selected and which ones are ignored. In this case, every number other than `1` is ignored. 

```python
fruits = ['apple', 'banana', 'pear']
transformed_elements = []

for current_element in fruits:
	transformed_elements.append(current_element + 's')

print(transformed_elements)
```

No `if` condition is necessary because the entire line is being selected (via iteration) to be transformed. In this case, an `s` is appended to each string in the `fruits` list.

One important thing to note is if the original collection is being mutated or if a new collection is being returned.

## Extracting Functions
```python
def selected_vowels(s):
	selected_chars = ''

	for char in s:
		if char in 'aeiouAEIOU':
			selected_chars += char

	return selected_chars
```

In this definition, a new string containing the selected characters is returned. This means other methods can be called or properties of the return value can be accessed.

```python
number_of_vowels = len(select_vowels('hello world'))
print(number_of_vowels)    # 3
```

### Practice Problem 1
```python
produce = {
	'apple': 'Fruit',
	'carrot': 'Vegetable',
	'pear': 'Fruit',
	'broccoli': 'Vegetable',
}

print(select_fruit((produce)))
```

In order to print only the fruits from the dictionary, an `if` statement can be used to determine which entries are selected and which ones are ignored.

```python
def select_fruit(produce_dict):
	fruit_dict = {}
	for item in produce_dict:
		if item.get() == 'Fruit':
			fruit_dict[item] == item.get()
	
	return fruit_dict
```

In this function, a new dictionary, `fruit_dict`, is declared to avoid direct mutation of the original collection. The `for` loop iterates through each item in the dictionary, and the `if` statement filters out any elements the appropriate values (in this case, `Fruit`). The filtered elements are added to the empty dictionary, which is returned at the end.

### Practice Problem 2
```python
def double_numbers(numbers):
	for current_index in len(numbers):
		numbers[current_index] *= 2

	return numbers
```

This function directly mutates the original collection (list) by doubling each element within the list. Each element is accessed by referencing the index of that number.

```python
def double_odd(numbers):
	doubled_nums = []

	for index in len(numbers):
		if numbers(index) % 2 != 0:
			doubled_nums.append(numbers[index] * 2)
		else:
			doubled_nums.append(numbers[index])

	return doubled_nums
```

In this function, a new list is created to avoid mutation. Elements in the list are accessed by iterating through them using a `for` loop. Odd numbers are filtered by using the `if` statement to check if the number is divisible by 2.

## More Flexible Functions
```python
def select_type(produce_list, selection_criterion):
	selected_items = {}

	for current_key, current_value in produce_list.items():
		if current_value == selection_criterion:
			selected_items[current_key] = current_value

	return selected_items
```

This  function uses a more generic function that is not specifically confined to only filtering out fruits. If the `selection_criterion` is set to `Vegetables`, it would return a new dictionary containing only the vegetables.

### Practice Problem
```python
def multiply(numbers, multiplier):
	multiplied_nums = []

	for number in numbers:
		multiplied_nums.append(number * multiplier)

	return multiplied_nums
```