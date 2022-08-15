# https://en.wikipedia.org/wiki/Fibonacci_number

from functools import lru_cache

import numpy as np

memory = {}

# normal
def fibo(n):
    print("doing fibo n =", n)
    if n < 2:
        return n

    if n in memory:
        return memory[n]
    else:
        result = fibo(n - 1) + fibo(n - 2)
        memory[n] = result
        return result


# faster
@lru_cache(maxsize=None)
def fibo2(n):
    print("doing fibo2 n =", n)
    if n < 2:
        return n
    return fibo2(n - 1) + fibo2(n - 2)


# fastest
def fibo3(n):
    F1 = np.array([[1, 1], [1, 0]], dtype="object")
    x = np.linalg.matrix_power(F1, n)
    return x[0][1]


# even fastest
def fibo4(n):
    F1 = np.array([[1, 1], [1, 0]], dtype="object")
    x = np.linalg.matrix_power(F1, n)
    return x[0][0]


if __name__ == "__main__":
    n = 10
    result = fibo(n)
    print(f"Result of the fibo = {n} is {result}")

    print(f"Trying method fibo2")
    print(fibo2(n))

    print("Trying fibo3")
    print(fibo3(n))

    print("Trying fibo4, since n-1 also give fibo(b) to the matrix")
    print(fibo4(n - 1))
