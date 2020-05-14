# 카드 역배치

arr = [x for x in range(0, 21)]

def swapReverse(arr, n, m):
    finalIdxToSwap = (n+m-1)//2
    for i in range(n, finalIdxToSwap+1):
        tmp = arr[i]
        arr[i] = arr[n+m-i]
        arr[n+m-i] = tmp

for _ in range(10):
    a, b = map(int, input().split())
    swapReverse(arr, a, b)

# 다른 풀이
# for _ in range(10):
#     for i in range((b-a+1)//2):
#         arr[a+i], arr[b-i] = arr[b-i], arr[a+i]


arr.pop(0)
for i in arr:
    print(i, end=' ')
