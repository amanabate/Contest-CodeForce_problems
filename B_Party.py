n = int(input())
managers = [int(input()) for _ in range(n)]

max_depth = 0

for i in range(n):
    depth = 1
    current = i
    while managers[current] != -1:
        depth += 1
        current = managers[current] - 1
    max_depth = max(max_depth, depth)

print(max_depth)