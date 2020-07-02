n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 오름차순 정렬
arr.sort()

# 이분 탐색
lt = 0
rt = n-1
while lt<=rt:
    mid = (lt+rt)//2
    if (arr[mid] == m):
        print(mid+1)
        break
    elif arr[mid]>m:
        rt = mid-1
    else:
        lt = mid+1



