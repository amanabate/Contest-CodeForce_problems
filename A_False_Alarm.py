t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    closed_indices = []
    for i in range(n):
        if a[i] == 1:
            closed_indices.append(i + 1)
    
    if not closed_indices:
        print("YES") 
    elif (closed_indices[-1] - closed_indices[0] + 1) <= x:
        print("YES")
    else:
        print("NO")