# Multiplicative Average
## Problem
Write a function that takes a list of positive integers as input, multiplies all of the integers together, divides the result by the number of the entries in the list, and returns the result as a string with the value rounded to three decimal places.

### Note
- Find the average after multiplying all items in a list
- Numbers must be rounded to three decimal places

## Example
```python
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
```

## Data
Data type involves lists and floats.

**Input: List**
**Output: Float**

## Algorithm
1. Initialize a product (1)
2. Iterate through the length of the list:
    - Multiply the value by the product and store it
3. Check if the length of the decimal is more than 3 places:
        - Round it to 3 places
    Else:
        - Pad with 0
4. Return the average of the product

## Code
```Python
def round_to_three(number):
    rounded_number_as_str = str(round(number, 3))
    decimal_position = rounded_number_as_str.find('.')

    while len(rounded_number_as_str) - decimal_position < 4:
        rounded_number_as_str += '0'

    return rounded_number_as_str

def multiplicative_average(num_list):
    product = 1
    for item in num_list:
        product *= item
    return round_to_three(product / len(num_list))
```