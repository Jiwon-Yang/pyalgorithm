# 대푯값

n = int(input())
arr = list(map(int, input().split()))

# 평균 구하기
rawAvg = sum(arr)/n
avg = int(rawAvg + 0.5) 
# round 는 round_half_even 방식을 택하기 때문


# 가장 가까운 수 구하기
# 다른 풀이
# minSub = 2147483647
# minIdx = 0
# for idx, val in enumerate(arr):
#     sub = abs(val - avg)
#     if(minSub > sub):
#         minIdx = idx
#         minSub = sub
#     elif(minSub == sub):
#         print(sub)
#         if(arr[minIdx] < arr[idx]):
#             minIdx = idx
#             minSub = sub
# print(avg, minIdx+1)


closestIdx = 0
for j in range(1, n):
    closestSub = arr[closestIdx] - avg
    nowSub = arr[j]-avg
    if(abs(closestSub)>abs(nowSub)):
        closestIdx = j
    elif(abs(closestSub)==abs(nowSub)):
        if(closestSub<nowSub):
            closestIdx = j        
print(avg, closestIdx+1)


