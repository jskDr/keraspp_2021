from typing import List

def binary_search(A:List[int], 
    l:int, h:int, x:int)->int:
    if h>=l:
        m = (l+h)//2
        if A[m]==x:
            return m
        elif A[m]>x:
            return binary_search(A,l,m-1,x)
        else:
            return binary_search(A,m+1,h,x)
    else:
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")