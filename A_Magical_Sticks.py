t = int(input())

for _ in range(t):
    sticks = int(input())
    if sticks == 1:
        print(1)
    else:
        print((sticks + 1) // 2)