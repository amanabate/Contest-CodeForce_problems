# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
    
  
#     if arr[0] == 0 and arr[-1] == 0:
#         # Check for consecutive 1's
#         has_11 = False
#         for i in range(n - 1):
#             if arr[i] == 1 and arr[i + 1] == 1:
#                 has_11 = True
#                 break
        
#         if not has_11:
#             print("Bob")
#         else:
#             print("Alice")
#     else:
#         print("Alice")


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(map(int, input().split()))
    
#     # Check if there are two consecutive 1's
#     has_consecutive_ones = False
#     for i in range(n - 1):
#         if arr[i] == 1 and arr[i + 1] == 1:
#             has_consecutive_ones = True
#             break
    
#     if has_consecutive_ones:
#         print("Alice")
#     else:

#         if arr[0] == 0 and arr[-1] == 0:
#             print("Bob")
#         else:
#             print("Alice")


def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # Count consecutive zeros at the start and end
        left_zeros = 0
        for i in range(n):
            if arr[i] == 0:
                left_zeros += 1
            else:
                break
        
        right_zeros = 0
        for i in range(n - 1, -1, -1):
            if arr[i] == 0:
                right_zeros += 1
            else:
                break
        
        # Alice wins if there's a zero at either end
        # or if the number of zeros between the first and last 1 is odd
        if left_zeros > 0 or right_zeros > 0:
            print("Alice")
        else:
            # Find first and last 1
            first_one = -1
            last_one = -1
            for i in range(n):
                if arr[i] == 1:
                    if first_one == -1:
                        first_one = i
                    last_one = i
            
            zeros_between = 0
            for i in range(first_one + 1, last_one):
                if arr[i] == 0:
                    zeros_between += 1
            
            if zeros_between % 2 == 1:
                print("Alice")
            else:
                print("Bob")

if __name__ == "__main__":
    solve()