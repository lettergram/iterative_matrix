import numpy as np
from scipy.linalg import solve

def gauss(A, b, x, n):

    L = np.tril(A)
    for i in range(n):
        x = x + np.dot(np.linalg.inv(L), b - np.dot(A, x))
        print str(i).zfill(3),
        print(x)
    return x

'''___MAIN___'''

A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [1.0, 2.0, 3.0]
x = [1, 1, 1]
n = 20

print("\n\ninit"),
print(x)
print("")
x = gauss(A, b, x, n)
print("\nSol "),
print(x)
print("Act "),
print solve(A, b)
print("\n")

