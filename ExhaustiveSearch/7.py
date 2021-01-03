import sys
sys.stdin = open('input.txt', 'r')

def DFS(level, sum):
    global minVal
    if level > minVal: #cut-tech
        return
    if sum > money:
        return
    if sum == money:
        if level < minVal:
            minVal = level
    else:
        for i in range(0, n):
            DFS(level+1, sum+arr[i])


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    money = int(input())

    minVal = 2147000000
    arr.sort(reverse=True)
    DFS(0, 0)
    print(minVal)

    