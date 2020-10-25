import sys
from collections import deque
sys.stdin = open("input.txt", "r")

n, maxWeight = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()
weights = deque(weights)

cnt = 0

while weights:
    if len(weights) == 1:
        cnt += 1
        break
    if weights[0] + weights[-1] <= maxWeight:
        cnt += 1
        p.popleft()
        p.pop()
    else:
        cnt += 1
        p.pop()

# solution 2
# l = 0
# r = n - 1
# while(l <= r):
#     if (l == r):
#         cnt += 1
#         break
#     if (weights[l] + weights[r] <= maxWeight):
#         l += 1
#     r -= 1
#     cnt += 1

print(cnt)
