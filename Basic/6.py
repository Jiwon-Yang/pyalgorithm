# 자릿수의 합

n = int(input())
arr = list(map(int, input().split()))
res = 0

def digit_sum(x):
    sum = 0
    while(x>0):
        remainder =  x%10
        sum += remainder
        x = x//10
    return sum

# 다른 방법
# def digit_sum(x):
#     sum = 0
#     for i in str(x):
#         sum += int(i)
#     return sum


max = -2147483647
for x in arr:
    sumVal = digit_sum(x)
    if(max<sumVal):
        max = sumVal
        res = x


print(res)
