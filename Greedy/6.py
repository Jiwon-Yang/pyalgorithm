import sys
sys.stdin = open("input.txt", "r")

n = int(input())
cnt = list(map(int, input().split()))
arr = [0 for _ in range(0, n)]
        
for i in range(n):
    for j in range(n):
        if cnt[i] == 0 and arr[j] == 0:
            arr[j] = i + 1
            break
        elif arr[j] == 0:
            cnt[i] -= 1

print(arr)



