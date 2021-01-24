import sys
sys.stdin = open('input.txt', 'r')

def DFS(level, s, sum):
    global cnt
    if level == k:
        if (sum % m) == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(level+1, i+1, sum+a[i])

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)