import numpy as np

def gauss_jordan(A, B):
    n = len(A)
    # Eliminasi Gauss
    for k in range(0, n-1):
        for i in range(k+1, n):
            if A[i, k] != 0:
                lam = A[i, k] / A[k, k]
                A[i, k:n] = A[i, k:n] - lam * A[k, k:n]
                B[i] = B[i] - lam * B[k]
                print('Matrik A:', '\n', A)

    # Substitusi
    x = np.zeros(n, float)
    for m in range(n-1, -1, -1):
        x[m] = (B[m] - np.dot(A[m, m+1:n], x[m+1:n])) / A[m, m]
        print('nilai X', m+1, '=', x[m])

# SPL 1
print("SPL 1:")
A1 = np.array([[1, 1, 1], [1, 2, -1], [2, 1, 2]], float)
B1 = np.array([6, 2, 10], float)
gauss_jordan(A1, B1)

# SPL 2
print("\nSPL 2:")
A2 = np.array([[1, 1], [2, 4]], float)
B2 = np.array([3, 8], float)
gauss_jordan(A2, B2)

# SPL 3
print("\nSPL 3:")
A3 = np.array([[3.7, 4, 0], [6, 2, 1], [2, -1, -3]], float)
B3 = np.array([45, 25, -15], float)
gauss_jordan(A3, B3)

# SPL 4
print("\nSPL 4:")
A4 = np.array([[2, 3, 1], [2, 1, 2], [3, 1, 2]], float)
B4 = np.array([9, 9, 11], float)
gauss_jordan(A4, B4)
