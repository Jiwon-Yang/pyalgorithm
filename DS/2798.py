# 파이썬 1초 약 2천만번 계산
n, m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0
length = len(data)

for i in (0, length):
    for j in (i+1, length):
        for k in (j+1, length):
            sum_value = data[i] + data[j] + data[k] # index와 원소 헷갈리지 않기!
            if(sum_value<=m):
                result = max(sum_value, result) # 둘 중에 큰 값 한번에 쓰기

