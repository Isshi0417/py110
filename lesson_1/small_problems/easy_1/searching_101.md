# Searching 101
*Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.*

## Example
```python
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.
```

- The 6th number is not printed in the latter half.
- The prompt is given in numeric form (1st, 2nd, 3rd, ...)

## Data
The solution could use either a list or a string since the output is mixed characters.

input = string (every input is a string)
output = string

## Algorithm
1. Initialize a `result` string to store 1st ~ 5th numbers
2. Initialize a `sixth` string to store the 6th number
3. Ask for the input:
	- Ask 'Enter the 1st number: ' and store the input to `result`
	- Repeat above for up to the 5th number
	- Ask 'Enter the last number:' and store the input to `sixth`
4. Check if `sixth` is in `result`
	- Print "`sixth` is in `result`" if the sixth number is within the first five
	- Print "`sixth` isn't in result" if the sixth number isn't within the first five
## Code
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