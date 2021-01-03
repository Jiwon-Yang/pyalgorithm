import sys
sys.stdin = open('input.txt', 'r')

def DFS(level, sum):
    if level == n and sum == f:
        for i in p:
            print(i, end=' ')
        print()
    else:
        for j in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[level] = i
                DFS(level+1, sum(p[level]*b[level]))
                ch[i] = 0

if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n
    b = [1] * n
    ch = [0] * (n+1)
    for i in range(1, n):
        b[i] = b[i-1] * (n-i) // i
    DFS(0, 0)