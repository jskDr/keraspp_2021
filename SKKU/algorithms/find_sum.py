

from typing import List

def FindSum(l: List[float], n: int) -> float:
    sum:float = 0.0;
    for i in range(0,n):
        sum += l[i];
    return sum


l:List[float] = [10.5, 4.8, 13.2, 6.4, 9.5]
n:int = 5
sum:float = FindSum(l, 3.5)

print(f"Sum = {sum}")