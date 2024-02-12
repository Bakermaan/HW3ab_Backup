def LUFactorization(A):
    """
    Perform LU factorization using Doolittle's method tailored for the provided matrix A.

    Args:
    A (list of lists): The input matrix A

    Returns:
    tuple: (L, U), where L is the lower triangular matrix with 1's on the diagonal, and U is the upper triangular matrix.
    """
    n = len(A)
    U = [[0] * n for _ in range(n)]
    L = [[0] * n for _ in range(n)]

    # Step 1: Initialize matrices L and U
    for i in range(n):
        U[0][i] = A[0][i]
        L[i][i] = 1

    # Step 2: Compute L and U
    for j in range(n):
        for i in range(j, n):
            U[j][i] = A[j][i] - sum(L[j][k] * U[k][i] for k in range(j))
        for i in range(j + 1, n):
            L[i][j] = (A[i][j] - sum(L[i][k] * U[k][j] for k in range(j))) / U[j][j]

    return (L, U)


def BackSolve(A, b, UT=True):
    """
    Perform back substitution tailored for the provided matrix A and vector b.

    Args:
    A (list of lists): Triangularized matrix (Upper or Lower)
    b (list): Right-hand side vector
    UT (bool): True if upper triangular, False if lower triangular

    Returns:
    list: Solution vector x
    """
    n = len(b)
    x = [0] * n

    if UT:
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
    else:
        for i in range(n):
            x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i))) / A[i][i]

    return x


def Doolittle(A, b):
    """
    Solve a system of linear equations using Doolittle's LU factorization method tailored for the provided matrix A and vector b.

    Args:
    A (list of lists): The input matrix A
    b (list): The right-hand side vector

    Returns:
    list: Solution vector x
    """
    L, U = LUFactorization(A)
    y = BackSolve(L, b, UT=False)
    x = BackSolve(U, y, UT=True)
    return x


def main():
    A = [
        [1, -1, 3, 2],
        [-1, 5, -5, -2],
        [3, -5, 19, 3],
        [2, -2, 3, 21]
    ]
    b = [15, -35, 94, 1]

    x = Doolittle(A, b)
    print("Solution vector x:", x)


if __name__ == "__main__":
    main()
