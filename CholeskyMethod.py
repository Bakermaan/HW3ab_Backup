def cholesky_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            sum_k = sum(L[i][k] * L[j][k] for k in range(j))

            if i == j:
                L[i][j] = (A[i][i] - sum_k) ** 0.5
            else:
                L[i][j] = (A[i][j] - sum_k) / L[j][j]
    return L

def forward_substitution(L, b):
    n = len(b)
    y = [0 for _ in range(n)]
    for i in range(n):
        sum_j = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_j) / L[i][i]
    return y

def backward_substitution(L, y):
    n = len(y)
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        sum_j = sum(L[j][i] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_j) / L[i][i]
    return x

if __name__ == "__main__":
    A = [
        [1, -1, 3, 2],
        [-1, 5, -5, -2],
        [3, -5, 19, 3],
        [2, -2, 3, 21]
    ]
    b = [15, -35, 94, 1]

    L = cholesky_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(L, y)
    print("Solution x:", x)
