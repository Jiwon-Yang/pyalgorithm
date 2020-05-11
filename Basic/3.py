# k번째로 큰 수

arrNum, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

arrToSet = set(arr)
setToArr = list(arrToSet)

print(setToArr[arrNum-k+1])

