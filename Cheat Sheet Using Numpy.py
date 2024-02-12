import numpy as np
from scipy.linalg import cholesky, lu, solve_triangular

# Define the matrix A and vector b
A = np.array([
    [4, 2, -3, 1],
    [6, 1, -1, 2],
    [-4, -3, 3, 0],
    [3, 1, 5, 2]
])

b = np.array([10, 20, -15, 25])

# Define a function to decide whether to use Cholesky or Doolittle (LU)
def solve_linear_system(A, b):
    try:
        # Attempt to perform a Cholesky decomposition, which requires the matrix to be symmetric positive definite
        L = cholesky(A, lower=True)
        # If successful, solve the system using the Cholesky decomposition
        y = solve_triangular(L, b, lower=True)
        x = solve_triangular(L.T, y)
        method_used = 'Cholesky'
    except np.linalg.LinAlgError:
        # If Cholesky decomposition fails, the matrix is not positive definite and we use LU decomposition instead
        P, L, U = lu(A)
        # Solve the system using LU decomposition
        y = solve_triangular(L, np.dot(P.T, b), lower=True)
        x = solve_triangular(U, y)
        method_used = 'Doolittle (LU)'

    return x, method_used

# Run the program and obtain the results
x, method_used = solve_linear_system(A, b)

# Print the solution and the method used
print(f"Solution x: {x}")
print(f"Method used: {method_used}")
