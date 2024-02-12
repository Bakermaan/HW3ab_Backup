import numpy as np

# Function to return colored text
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[0m".format(r, g, b, text)

def is_symmetric_with_transpose(matrix):
    n = len(matrix)
    transpose = [[matrix[j][i] for j in range(n)] for i in range(n)]
    return all(matrix[i][j] == transpose[i][j] for i in range(n) for j in range(n))

def is_symmetric_optimized(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_symmetric_zip(matrix):
    return all(row[i] == col for i, row in enumerate(zip(*matrix)) for col in row)

def is_symmetric_numpy(matrix):
    np_matrix = np.array(matrix)
    return np.array_equal(np_matrix, np_matrix.T)

def print_result(method_name, result):
    color = (0, 255, 0) if result else (255, 0, 0)  # Green if True, Red if False
    print(f"{method_name}: {colored(*color, result)}")

# Define the matrix to test
matrix = [
    [1, -1, 3, 2],
    [-1, 5, -5, -2],
    [3, -5, 19, 3],
    [2, -2, 3, 21]
]

# Running all symmetry checks with colored output
print("Checking symmetry using various methods:")
print_result("1. Direct Comparison with Transpose", is_symmetric_with_transpose(matrix))
print_result("2. Half Matrix Comparison (Optimized)", is_symmetric_optimized(matrix))
print_result("3. Row-Column Zip Comparison", is_symmetric_zip(matrix))
print_result("4. Using NumPy", is_symmetric_numpy(matrix))
