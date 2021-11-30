from numba import jit, int32

@jit(int32(int32))
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)

print(fibo(45))