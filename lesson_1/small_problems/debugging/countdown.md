# Countdown
## Problem
Our countdown to launch isn't behaving as expected. Why? Change the code so that our program successfully counts down from 10 to 1 before launching.

```python
def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    decrease(counter)

print('LAUNCH!')
```

## Answer
The program doesn't launch behave as expected `counter` is not reassigned the lesser value. This can be achieved by simply assigning `counter = decrease(counter)`.