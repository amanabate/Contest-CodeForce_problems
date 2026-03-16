t = int(input())

for _ in range(t):
    k, x = map(int, input().split())
    
    for _ in range(k):
        if x % 6 == 4:
            x = (x - 1) // 3
        else:
            x = x * 2

    print(x)
