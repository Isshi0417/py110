# Searching 101
*Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.*

```python
def check_six():
	result = ''
	sixth = ''

	for i in range(6):
		if i == 0:
			result += ',' + input('Enter the 1st number: ')
		elif i == 1:
			result += ',' + input('Enter the 2nd number: ')
		elif i == 2:
			result += ',' + input('Enter the 3rd number: ')
		elif i == 5:
			sixth = input('Enter the last number: )
		else:
			result += ',' + input(f'Enterthe {i + 1}th number:')

	if sixth in result:
		print(f'{sixth} is in {result}')
	else:
		print(f'{sixth} isn\'t in {result}')
```