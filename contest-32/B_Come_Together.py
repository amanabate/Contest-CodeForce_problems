t = int(input())

for _ in range(t):
    xA, yA = map(int, input().split())
    xB, yB = map(int, input().split())
    xC, yC = map(int, input().split())

    dx = min(abs(xA - xB), abs(xA - xC))
    dy = min(abs(yA - yB), abs(yA - yC))

    print(min(dx, dy) + 1)
