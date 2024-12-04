# Unlucky Days
## Problem
Some people believe that Fridays that fall on the 13th day of the month are unlucky days. Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in use for the foreseeable future.

## Example
```python
print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
```

## Data
Data handled are integers and date.

**Input**: Integer
**Intermediate Steps**: Date
**Output**: Integer

## Algorithm
1. Import datetime.date
2. iterate over all the months of the given year
3. For each month, get the day that falls on the 13th:
    - Count the 13ths that fall ona friday
4. Return count

## Code
```python
import datetime

def friday_the_13ths(year):
    count = 0
    thirteenth = []

    for month in range(1, 13):
        thirteenth.append(datetime.date(year, month, 13))

    for day in thirteenth:
        if day.weekday() == 4:
            count += 1
    
    return count
```