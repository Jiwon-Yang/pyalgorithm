# 수들의 합

n, m = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in range(n):
    sumVal = 0
    for j in range(i, n):
        sumVal += arr[j]
        if sumVal==m:
            count += 1
            break
        elif sumVal>m:
            break

print(count)



