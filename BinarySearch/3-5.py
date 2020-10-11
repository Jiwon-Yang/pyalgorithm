import sys
input = sys.stdin.readline
N,M = map(int,input().split())
L = []
for _ in range(N):
    L.append(int(input()))

def binarySearch(a, m, M):
    low,sum,r = 1,0,0
    high = m
    while low <= high:
        mid = (low + high) // 2
        for i in a:
            sum += i//mid
        if(sum >= M):
            low = mid + 1
            r = mid
            sum = 0
        else:
            high = mid - 1
            sum = 0
    return r

print(binarySearch(L, max(L), M))