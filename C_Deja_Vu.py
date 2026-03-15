import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    g = list(map(int, input().split()))
    
    heapq.heapify(g)
    cost = 0
    
    while len(g) > 1:
        a = heapq.heappop(g)
        b = heapq.heappop(g)
        
        cost += b
        heapq.heappush(g, b - a)
    
    print(cost)
