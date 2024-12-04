# Egyptian Fractions
## Problem
Write **two** functions: one takes a rational number as an argument and returns a list of the denominators that are part of an Egyptian Fraction representation of the number, and another that takes a list of numbers in the same format and calculates the resulting rational number. You will need to use the `Fraction` class provided by the `fractions` module.

## Example
```python
from fractions import Fraction

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))
```

## Data
Data handled are fractions and integers (lists).

**Input**: Integer
**Intermediate Steps**: Fraction
**Output**: List/Fraction

## Algorithm
1. Initialize denominators
2. Initialize unit denominator
3. While target value is not 0:
    - Unit fraction = 1/denominator
    - if unit fraction is less than target value:
        - subtract unit fraction from target value
        - add t he unit denominator to the list
    - increment unit denominator
4. Return denominators

## Code
```python
from fractions import Fraction

def egyptian(target):
    result = []
    unit_denominator = 1
    while target != 0:
        unit_fraction = Fraction(1, unit_denominator)
        if unit_fraction <= target:
            target -= unit_fraction
            result.append(unit_denominator)
    unit_denominator += 1

    return result

def unegyptian(denominators):
    return sum([Fraction(1,d) for d in denominators])
```