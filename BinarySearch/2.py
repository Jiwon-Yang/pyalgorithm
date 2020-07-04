# K 값이 될 수 있는 값
# 최소값 = 1
# 최댓값 = 802 
# 이때 mid = 401 
# -> mid로 각각의 막대기를 자르면 N을 충족하는지 확인
import sys
sys.stdin = open("input.txt", "r")

def count(length):
    sumVal = 0
    for j in range(k):
        sumVal += (arr[j]//length)
    return sumVal

# 입력 받기 & 오름차순 정렬
k, n = map(int, input().split())
arr = []
largest = 0
for i in range(k):
    tmp = int(input())
    arr.append(tmp)
    largest = max(largest, tmp)

# Binary Search
maxVal = 0
lt = 1
rt = largest

while lt<=rt:
    mid = (lt+rt)//2
    rodNum = count(mid)
    if rodNum >= n:
        maxVal = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(maxVal)

    


        