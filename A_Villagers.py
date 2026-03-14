import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    g = list(map(int, input().split()))
    
    g.sort()
    
    ans = 0
    prefix_sum = 0
    for i in range(1, n):
        ans += g[i] * i - prefix_sum
        prefix_sum += g[i]
    
    print(ans + g[0])