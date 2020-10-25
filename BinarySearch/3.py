import sys
sys.stdin = open('input.txt', 'r')

def count(capacity):
    cnt = 1
    sum = 0
    for x in music:
        if sum + x > capacity:
            cnt += 1
            sum = 0
        else:
            sum += x
    return cnt



n, m = map(int, input().split())
music = list(map(int, input().split()))

lt = 1
rt = sum(music)
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) <= m:
        res = mid
        rt = mid -1
    else:
        lt = mid + 1

print(res)
