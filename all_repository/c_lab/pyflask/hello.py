print("Hello World!")

# sum elements of list of a
a = [1, 2, 3]
s = 0
for x in a:
    s = s + x
    print(s, x)

# sum from 0 to 9
s = 0
for x in range(10):
    s = s + x
    print(s, x)

# function to calculate a factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

ans = factorial(10)
print(f"factorial(10)={ans}")
