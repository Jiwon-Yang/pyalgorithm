#격자 판 최대합

n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]
largest = -2147483647

# for x in arr:
#     print(x)

# 가로, 세로 합

for i in range(n):
    sum1 = 0
    sum2 = 0
    for j in range(n):
        sum1 += arr[i][j]
        sum2 += arr[j][i]
    if sum1 > largest:
        largest = sum1 
    if sum2 > largest:
        largest = sum2

# 대각선 합
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += arr[i][i]
    sum2 += arr[i][n-i-1]
if sum1 > largest:
    largest = sum1 
if sum2 > largest:
    largest = sum2

