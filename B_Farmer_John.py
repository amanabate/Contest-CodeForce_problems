import sys

input = sys.stdin.read
data = input().split()
idx = 0
t = int(data[idx]); idx += 1
out = []

for _ in range(t):
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    req = []
    for __ in range(n):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        req.append((a, b))
    
    points = 0
    pos = 0
    prev_time = 0
    prev_side = 0
    
    for i in range(n):
        a, b = req[i]
        time_diff = a - prev_time
        moves = time_diff
        
        if pos == prev_side:
            if b == pos:
                points += moves
                pos ^= 1
            else:
                if moves >= 1:
                    points += 1
                    pos = b
                    moves -= 1
                    if b == 1:
                        points += moves
                        pos ^= 1
                    else:
                        points += moves
                else:
                    pos = b
        else:
            if b == pos:
                if moves >= 1:
                    points += 1
                    pos = b
                    moves -= 1
                    if b == 1:
                        points += moves
                        pos ^= 1
                    else:
                        points += moves
                else:
                    pos = b
            else:
                points += moves
                pos = b
        
        prev_time = a
        prev_side = b
    
    if m > prev_time:
        moves = m - prev_time
        if pos == prev_side:
            points += moves
        else:
            if moves >= 1:
                points += 1
                moves -= 1
                points += moves
    
    out.append(str(points))

print("\n".join(out))