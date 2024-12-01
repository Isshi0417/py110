# Cute Angles
## Problem
Write a function that takes a floating number repreenting an angle between 0 and 360 degrees and returns a string represengint that angle in degrees, minutes, and seconds. You should use degree sumbol(°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes ina a degree, and 60 seconds in a minute.

Note:  You can use the following constant to represent the degree symbol:
```python
DEGREE = "\u00B0"
```

### Questions
- What does the problem mean by minutes and degrees from an angle?
- Do negative angles need to be accounted for?
- How are the minutes and seconds calculated?

## Example
```python
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
```

### Clarifications
- The minutes and seconds are calculated in percentagees
- Negative angles can be ignored

## Data
Data type handled are strictly floats and strings.

**Input: Float**
**Output: String**

## Algorithm
1. Initialize degree, minute, and second constants.
2. Take the float:
    1. Set degree to the integer portion
    2. Set minute to (float - integer) * 60
    3. Set seconds to (float - integer - (minutes / 60)) * 60
    4. Print the results
        - Print degree
        - Print minutes
            1. If the number is only one digit:
                - Pad the number with 0
        - Print second
            1. If the number is only one digit:
                - Pad the number with 0

## Code
```python
# Constants
DEGREE = "\u00B0"
MINUTES_PER_DEGREE = 60
SECONDS_PER_MINUTE = 60
SECONDS_PER_DEGREE = MINUTES_PER_DEGREE * SECONDS_PER_MINUTE

def pad_zeroes(number):
    num_string = str(number)
    if len(num_string) < 2:
        return '0' + num_string
    else:
        return num_string

def dms(degrees_float):
    degrees_int = int(degrees_float)
    minutes = int((degrees_float - degrees_int) * MINUTES_PER_DEGREE)
    seconds = int(
        (degrees_float - degrees_int - (minutes / MINUTES_PER_DEGREE)) *
        SECONDS_PER_DEGREE
    )

    return (
        f"{degrees_int}{DEGREE}"
        f"{pad_zeroes(minutes)}'"
        f'{pad_zeroes(seconds)}"'
    )
```