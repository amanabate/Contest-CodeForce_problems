t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    possible = True
    for i in range(n):
        if a[i] % 2 != (i + 1) % 2:
            possible = False
            break
    
    print("YES" if possible else "NO")