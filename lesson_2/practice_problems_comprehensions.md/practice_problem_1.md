# Practice Problem 1
## Problem
Consider the following nested dictionary:

```python
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
```

Compute and display the total age of the family's male members. try working out the answer with an ordinary loop, then with a comprehension.

## Solution
```python
# For Loop
total_age = 0
for name, info in munsters.items():
    if info["gender"] == "male":
        total_age += info["age"]
print(total_age)

# Comprehension
male_ages = [info["age"] for name, info in munsters.items() 
             if info["gender"] == "male"]

print(sum(male_ages))
```