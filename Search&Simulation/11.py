import sys
sys.stdin = open('input.txt', 'r')
arr = [ list(map(int, input().split())) for _ in range(7) ]
cnt = 0

for i in range(3):
    for j in range(7):
        tmp = arr[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt += 1
        tmp2 = arr[i][j]

print(cnt)
        