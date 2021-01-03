import sys
sys.stdin = open('input.txt', 'r')

def DFS(level, sum):
    if sum > (total//2):
        return
    if level == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(level+1, sum+numArr[level])
        DFS(level+1, sum)


if __name__ == "__main__":
    n = int(input())
    numArr = list(map(int, input().split()))
    total = sum(numArr)
    DFS(0, 0)
    print("NO")