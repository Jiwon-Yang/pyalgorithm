#격자 판 최대합

n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]
max = -2147483647

# 행 max 비교
for i in range(n):
    sum = 0
    for j in arr[i]:
        sum += j
    if(sum>max):
        max = sum

# 열 max 비교
for i in range(n):
    sum = 0
    for j in range(n):
        sum += arr[j][i]
    if(sum>max):
        max = sum

# 대각선 max 비교 1
sum = 0
for i in range(n):
    for j in range(n):
        if i==j:
            sum += arr[i][j]
if(sum>max):
    max = sum

# 대각선 max 비교 2
for i in range(n):
    for j in range(n):
        if i+j==n:
            sum += arr[i][j]
if(sum>max):
    max = sum


print(max)
    