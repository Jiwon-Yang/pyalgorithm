import sys
sys.stdin = open("input.txt", "r")

n = int(input())
boxes = list(map(int, input().split()))
sortNum = int(input())

for _ in range(sortNum):
    boxes.sort()
    boxes[0] += 1
    boxes[n-1] -= 1

boxes.sort()
print(boxes[n-1] - boxes[0])
