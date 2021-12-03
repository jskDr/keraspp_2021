from numba import jit

@jit
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(45))