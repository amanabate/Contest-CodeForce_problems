t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
  
    if arr[0] == 0 and arr[-1] == 0:
        # Check for consecutive 1's
        has_11 = False
        for i in range(n - 1):
            if arr[i] == 1 and arr[i + 1] == 1:
                has_11 = True
                break
        
        if not has_11:
            print("Bob")
        else:
            print("Alice")
    else:
        print("Alice")