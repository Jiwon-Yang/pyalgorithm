# k번째로 작은 수

tc = int(input())

for i in range(tc):
    N, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    print("#%d %d" %(i+1, arr[k-1]))

