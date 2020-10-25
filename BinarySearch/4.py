import sys
sys.stdin = open('input.txt', 'r')

def count(len):
    cnt = 1
    ep = locations[0]
    for i in range(1, n):
        if locations[i] - ep >= len :
            cnt += 1
            ep = locations[i]
    return cnt

n, c = map(int, input().split())
locations = []
for _ in range(n):
    tmp = int(input())
    locations.append(tmp)

locations.sort()

lt = 1
rt = locations[n-1]
res = 0

while lt<=rt:
    mid = (lt+rt)//2
    if count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
    
print(res)


