t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    Rgold = 0
    given = 0

    for i in a:
        if i >= k:
            Rgold += i
        elif i == 0 and Rgold > 0:
            Rgold -= 1
            given += 1

    print(given)
