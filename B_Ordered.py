# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     possible = True
#     for i in range(n):
#         if a[i] % 2 != (i + 1) % 2:
#             possible = False
#             break
    
#     print("YES" if possible else "NO")


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    
    visited = [False] * (n + 1)
    ok = True
    
    for i in range(1, n + 1):
        if not visited[i]:
            indices = []
            j = i
            
            # collect component
            while j <= n:
                visited[j] = True
                indices.append(j)
                j *= 2
            
            # collect values
            vals = [a[x] for x in indices]
            
            # sort both
            indices.sort()
            vals.sort()
            
            # check if can match sorted positions
            for idx, val in zip(indices, vals):
                if val != idx:
                    ok = False
                    break
            
            if not ok:
                break
    
    print("YES" if ok else "NO")
