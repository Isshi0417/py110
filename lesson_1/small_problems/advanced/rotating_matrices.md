# Rotating Matrices
## Problem
Write a function that takes an arbitrary MxN matrix, rotates it clockwise by 90-degrees as described above, and returns the result as a new matrix. The function should not mutate the original matrix.

## Example
```python
matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)
```

## Data
Data handled are lists.

**Input**: List of lists
**Output**: List of lists

## Algorithm
1. Initialize an empty matrix
2. Transpose the matrix
3. Reverse the row
4. Return the result

## Code
```python
def rotate90(matrix):
    result = []
    rows = len(matrix[0])

    for _ in range(rows):
        result.append([])

    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[row_index])):
            result[column_index].append(matrix[row_index][column_index])

    for row in result:
        row.reverse()

    return result
```