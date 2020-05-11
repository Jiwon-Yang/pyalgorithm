# 3개를 합한 값에서 k번째로 큰 수

n, k = map(int, input().split())
arr = list(map(int, input().split()))

res = set()

for i in range(0, n):
    for j in range(i+1, n):
        for l in range(j+1, n):
            sum = arr[i] + arr[j] + arr[l]
            res.add(sum)

resArr = list(res)
resArr.sort(reverse=True)
print(resArr[k-1]) 

