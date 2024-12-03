# Inventory Item Transactions
## Problem
Write a function that takes two arguments, an inventory item ID, and a list of transactions, and returns a list containing only the transactions for the specified inventory item.

## Example
```python
transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True
```

## Data
Data handled is a list of dictionaries.

**Input**: List
**Output**: List

## Algorithm
1. Initialize an empty list
2. Iterate through each item:
    - If the item ID is equal to 101:
        1. Append to empty list
3. Return the list

## Code
```python
def transactions_for(id, transactions):
    result = []
    for item in transactions:
        if item["id"] == id:
            result.append(item)
    return result
```