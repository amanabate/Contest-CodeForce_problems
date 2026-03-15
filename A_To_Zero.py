
t = int(input())
answer = []
for _ in range(t):
    n, k = map(int, input().split())
    if n % 2 == 0:  
        ans = (n + k - 2) // (k - 1)
    else:
        if n <= k:
            ans = 1
        else:
            ans = 1 + (n - 2) // (k - 1)
    answer.append(str(ans))
print("\n".join(answer))

