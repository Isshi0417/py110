# After Midnight (Part 1)
## Problem
The time of the day can be represented as the number of minutes before
or after midnight. If the number of minutes is positive, the time is
after midnight. if the number of minutes is negative, the time is
before midnight.

Write a function that takes a time using this minute based-format and 
returns the time of the day in 24-hour format (hh:mm). Your function 
should work with any integer input.

You may not use Python's `datetime` module.

### Notes
- Find the current time based on the given number of minutes.
- Must be on 24 hour clock.

### Questions
- Does the output need to follow a specific format?

## Example
```python
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
```

### Clarifications
- The format needs to be hh:mm.

## Data
Data handled are strictly integers and strings.

**Input: Integer**
**Output: String**

## Algorithm
1. Set time constants
2. While minute difference is less than 0:
    - minute difference += minutes per day
3. Set minute difference to the remainder of the quotient between 
minute difference and minutes per day.
4. Set hours to minute difference divided by minutes per hour
5. Set minutes to the remainder of time difference and minutes per 
hour.
6. Return formatted time.

## Code
```python
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def format_time(hours, minutes):
    return f"{hours:02d}:{minutes:02d}"

def time_of_day(delta_minutes):
    while delta_minutes < 0:
        delta_minutes += MINUTES_PER_DAY

    delta_minutes = delta_minutes % MINUTES_PER_DAY
    hours = delta_minutes // MINUTES_PER_HOUR
    minutes = delta_minutes % MINUTES_PER_HOUR

    return format_time(hours, minutes)
```