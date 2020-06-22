n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]

res = 0
s=e=n//2

for i in range(n):
    for j in range(s, e+1):
        res += arr[i][j]
    if i<n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

# mid = n//2
# for i in range(mid):
#     for j in range(mid-i, mid+i+1):
#         res += arr[i][j]
# for i in range(mid, n):
#     dis = n - i - 1
#     for j in range(mid-dis, mid+dis+1):
#         res += arr[i][j]




print(res)
        