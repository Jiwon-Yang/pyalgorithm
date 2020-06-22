n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]
dx = [-1, 0, 1, 0 ]
dy = [0, 1, 0, -1]
res = 0

# 가장자리 추가
arr.insert(0, [0]*n)
arr.append([0]*n)

for i in range(n+2):
    arr[i].insert(0, 0)
    arr[i].append(0)


# 봉우리 계산
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(arr[i][j]>arr[i+dx[k]][j+dy[k]] for k in range(4)):
            res += 1

print(res)
