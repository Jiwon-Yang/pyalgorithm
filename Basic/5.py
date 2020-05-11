# 정다면체

n, m = map(int, input().split())
cnt = [0 for _ in range(n+m+1)]
sumVal = 0
maxVal = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        sumVal = i + j
        cnt[sumVal] += 1

for k in range(1, n+m+1):
    if(maxVal<cnt[k]):
        maxVal = cnt[k]

for l in range(1, n+m+1):
    if(maxVal == cnt[l]):
        print(l, end=' ')
