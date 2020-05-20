# 수들의 합

n, m = map(int, input().split())
arr = list(map(int, input().split()))

sumVal = arr[0]
count = 0

left = 0
right = 1

while True :
    if sumVal==m:
        count += 1
        sumVal -= arr[left]
        left += 1
    elif sumVal<m:
        if right<n:
            sumVal += arr[right]
            right += 1
        else:
            break
    else:
        sumVal -= arr[left]
        left += 1
        
    

print(count)



