

def gcd(L:int, S:int)->int:
    while S>0:
        R = L % S
        L = S
        S = R
    return L

print(gcd(50,30))