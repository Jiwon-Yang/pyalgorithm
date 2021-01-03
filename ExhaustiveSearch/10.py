import sys
sys.stdin = open('input.txt', 'r')

def DFS(level, sum):
    global cnt
    if level == m:
        for j in range(level):
            print(res[j], end=' ')
        cnt += 1
        print()
    else:
        for j in range(1, n+1):
            res[level] = i
            DFS(level+1, i+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * (n+1)
    cnt = 0
    DFS(0, 1)
    print(cnt)