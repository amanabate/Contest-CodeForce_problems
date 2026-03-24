n = int(input())

r = list(map(int, input().split()))
b = list(map(int, input().split()))

A = 0  # Robo-Coder
B = 0  # BionicSolver 

for i in range(n):
    if r[i] == 1 and b[i] == 0:
        A += 1
    elif r[i] == 0 and b[i] == 1:
        B += 1

if A == 0:
    print(-1)

else:
    # Increase points on Robo-only 
    M = 1
    while A * M <= B:
        M += 1
        
    print(M)
