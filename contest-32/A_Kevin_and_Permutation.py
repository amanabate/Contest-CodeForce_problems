t = int(input())

for _ in range(t):
    n = int(input())
    d = n // 2
    res = []

    for i in range(n):
        if i % 2 == 0:
            res.append(d + 1 + i // 2)
        else:
            res.append(i // 2 + 1)
            
    print(*res)