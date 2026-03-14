t = int(input())

for _ in range(t):
    n = int(input())

    s = input().strip()
    u_count = s.count('U')
    
    if u_count % 2 == 1:
        print("YES")
    else:
        print("NO")