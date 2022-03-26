

sum:int = 0
n:int = 10
    
for i in range(n): 
    for j in range(i):  
        for k in range(j):
                sum += 1

print(f"Total complexiity: {sum}")


