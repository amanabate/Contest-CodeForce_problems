t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    possible = False
    for i in range(n):
        if arr[i] == 67:
            possible = True
            break
        for j in range(i + 1, n):
            if arr[i] * arr[j] == 67:
                possible = True
                break
        if possible:
            break
    print("YES" if possible else "NO")