import sys
sys.stdin = open("input.txt", "r")

n = int(input())
players = []
for i in range(n):
    h, w = map(int, input().split())
    players.append((h, w))

players.sort(reverse=True)

largest = 0
cnt = 0
for h, w in players:
    if w > largest:
        cnt += 1
        largest = y

print(cnt)