import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def DFS(level, sum, tsum):
    global result
    if sum + (total-tsum) < result:
        return
    if sum > c:
        return
    if level == n:
        if result < sum:
            result = sum
    else:
        DFS(level+1, sum+baduks[level], tsum+baduks[level])
        DFS(level+1, sum, tsum+baduks[level])

if __name__ == "__main__":
    result = -2147000000
    c, n = map(int, input().split())
    baduks = []
    for _ in range(n):
        baduks.append(int(input()))
    total = sum(baduks)
    DFS(0, 0, 0)
    print(result)
