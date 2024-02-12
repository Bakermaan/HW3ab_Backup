def gauss_seidel(aug_matrix, initial_guess, tolerance=1e-10, max_iterations=1000):
    """
    Performs Gauss-Seidel iteration to solve the system of linear equations A*x = b.

    :param aug_matrix: The augmented matrix [A|b] of the system.
    :param initial_guess: The initial guess for the solution.
    :param tolerance: The tolerance for the stopping criterion.
    :param max_iterations: The maximum number of iterations.
    :return: The approximate solution vector.
    """
    # Separate the augmented matrix into A and b
    A = [row[:-1] for row in aug_matrix]
    b = [row[-1] for row in aug_matrix]
    n = len(b)
    x = initial_guess
    for iteration in range(max_iterations):
        x_new = x[:]
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        # Stopping condition
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            return x_new
        x = x_new
    raise ValueError(f"Gauss-Seidel method did not converge after {max_iterations} iterations.")

# Function to separate the augmented matrix into A and b
def separate_augmented(aug_matrix):
    A = [row[:-1] for row in aug_matrix]
    b = [row[-1] for row in aug_matrix]
    return A, b

# Function to check the solution
def check_solution(aug_matrix, solution):
    A, b = separate_augmented(aug_matrix)
    return all(abs(sum(A[i][j] * solution[j] for j in range(len(solution))) - b[i]) < 1e-10 for i in range(len(b)))

# Function to multiply matrices
def matrix_mult(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        raise ValueError("Cannot multiply the two matrices. Incorrect dimensions.")
    # Create the result matrix
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
