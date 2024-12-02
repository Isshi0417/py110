# After Midnight (Part 2)
## Problem
As seen in the previous exercise, the time of the day can be 
represented as the number of minutes before or after midnight. If the 
number of minutes is positive, the time is after midnight. If the 
number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, 
and return the number of minutes before and after midnight, 
respectively. Both functions should return a value in the range `0` 
through `1439`.

You may not use Python's `datetime` module.

### Notes
- Time of the day needs to be expressed in 24 hour format.
- The functions should not return any number that exceeds 0 and 1439.

## Example
```python
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
```

## Data
Data handled is strictly strings and integers.

**Input: String**
**Output: Integer**

## Algorithm
1. Set time constants
2. After midnight:
    1. Split the string along ":"
    2. Return the time in minutes
3. Before midnight:
    1. Split the string along ":"
    2. Check if time difference is equal to minutes per day:
        - Set time difference to 0
    3. Return the time in minutes

## Code
```python
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def after_midnight(time_str):
    hours, minutes = [int(unit) for unit in time_str.split(":")]
    return ((hours * MINUTES_PER_HOUR) + minutes) % MINUTES_PER_DAY

def before_midnight(time_str):
    delta_minutes = MINUTES_PER_DAY = after_midnight(time_str)
    if delta_minutes == MINUTES_PER_DAY:
        delta_minutes = 0

    return delta_minutes
```