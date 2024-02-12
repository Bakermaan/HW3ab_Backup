from CholeskyMethod import cholesky_decomposition
from DoolittleMethod import LUFactorization
import copy
from user_input_handler import get_user_input

def transpose_matrix(L):
    """Transpose a square matrix."""
    return [list(i) for i in zip(*L)]

def forward_substitution(L, b):
    """Solve Ly = b."""
    y = [0 for _ in range(len(b))]
    for i in range(len(b)):
        sum_j = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_j) / L[i][i]
    return y

def backward_substitution(U, y):
    """Solve Ux = y."""
    x = [0 for _ in range(len(y))]
    for i in reversed(range(len(y))):
        sum_j = sum(U[i][j] * x[j] for j in range(i+1, len(y)))
        x[i] = (y[i] - sum_j) / U[i][i]
    return x

def solve_system(A, b):
    """Determine the method and solve the system."""
    original_A = copy.deepcopy(A)
    original_b = copy.deepcopy(b)
    if is_symmetric(original_A) and is_positive_definite(original_A):
        method = 'Cholesky'
        L = cholesky_decomposition(original_A)
        y = forward_substitution(L, original_b)
        x = backward_substitution(transpose_matrix(L), y)
    else:
        method = 'Doolittle'
        L, U = LUFactorization(original_A)
        y = forward_substitution(L, original_b)
        x = backward_substitution(U, y)
    return x, method

def is_symmetric(matrix, tolerance=1e-9):
    """Check symmetry."""
    return all(abs(matrix[i][j] - matrix[j][i]) < tolerance for i in range(len(matrix)) for j in range(i+1, len(matrix)))

def is_positive_definite(matrix):
    """Placeholder for positive definiteness check."""
    # Implement the check or use cholesky_decomposition in a try-except block
    try:
        cholesky_decomposition(matrix)
        return True
    except:
        return False

def main():
    """Main function to run the program."""
    try:
        A, b = get_user_input()
        x, method_used = solve_system(A, b)
        print("\nMethod used:", method_used)
        print("Solution x:", x)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
