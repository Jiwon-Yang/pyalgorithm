import sys
sys.stdin = open('input.txt', 'r')

def DFS(level):
    global cnt
    if level == m:
        for i in range(m):
            print(res[i], end=' ')
        cnt += 1
        print()
    else:
        for j in range(1, n+1):
            if ch[j] == 0:
                ch[j] = 1
                res[level] = j
                DFS(level+1)
                ch[j] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    ch = [0] * (n+1)
    cnt = 0
    DFS(0)
    print(cnt)