# 점수 계산

n = int(input())
arr = list(map(int, input().split()))
res = 0
addVal = 0

for x in arr:
    if x==1:
        addVal += 1
        res += addVal
    else:
        addVal = 0

print(res)