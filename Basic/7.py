# 소수 (에라토스테네스 체)
# i는 2부터 N까지로서, i의 배수의 index의 value 값을 1로 바꿔줌

n = int(input())
arr = [0] * (n+1)

# 다른 풀이 (by 지원)
# for i in range(2, n):
#     for j in range(2, 200000):
#         print(i*j)
#         if(i*j <= (n+1)):
#             arr[i*j] = 1
#         else:
#             break
# count = 0
# for k in range(2, n+1):
#     if(arr[k] == 0):
#         count += 1

count = 0
for i in range(2, n+1):
    if(arr[i] == 0):
        count += 1
    for j in range(i, n+1, i):
        arr[j] = 1


print(count)