n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]
m = int(input()) # 명령 개수

# 명령 수행
for _ in range(m):
    row, direction, offset = map(int, input().split())
    if direction == 0:
        for _ in range(offset):
            arr[row-1].append(arr[row-1].pop(0))
    else:
        for _ in range(offset):
            arr[row-1].insert(0, arr[row-1].pop())


# 모래시계 모양으로 더함
s = 0
e = n
sumVal = 0

for i in range(n):
    for j in range(s, e):
        sumVal += arr[i][j]
    if i < n//2 :
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
    
print(sumVal)

