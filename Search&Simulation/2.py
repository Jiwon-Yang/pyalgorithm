# 숫자만 추출
# isdecimal() isdigit()
word = input()
res = 0
count = 0

for x in word :
    if x.isdecimal():
        res = res*10 + int(x)

res = int(res)
print(res)

for i in range(1, res+1):
    if res%i==0:
        count += 1

print(count)




