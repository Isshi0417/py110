# Transpose 3x3 Matrix
## Problem
A 3x3 matrix can be represented by a list of nested lists: an outer list that contains three sub-lists that each contain three elements. For example, the 3x3 matrix shown below:

```
1  5  8
4  7  2
3  9  6
```

is represented by the following list of lists:

```python
matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]
```

The transpose of a 3x3 matrix is the matrix that results from exchanging the rows and columns of the original matrix.For example, the transposition of the matrix shown above is:

```
1  4  3
5  7  9
8  2  6
```

Write a function that takes a list of lists that represents a 3x3 matrix and returns the transpose of the matrix. You should implement the function on your own without using any external libraries.

Take care not to modify the original matrix -- your function must produce a new matrix and leave the input `matrix` list unchanged.

## Example
matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

## Data
Data handled is simply a list.

**Input**: List of lists
**Output**: List of lists

## Algorithm
1. Initialize a new empty matrix
2. For each row:
    - For each column:
        - Append the value to the matrix
3. Return the result

## Code
```python
def transpose(matrix):
    result = []
    rows = len(matrix[0])

    for _ in range(rows):
        result.append([])

    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[row_index])):
            result[column_index].append(matrix[row_index][column_index])

    return result
```