# 두 리스트 합치기

aLen = int(input())
a = list(map(int, input().split()))
bLen = int(input())
b = list(map(int, input().split()))

p1 = 0
p2 = 0
res = []

while p1<aLen and p2<bLen:
    if a[p1]>b[p2]:
        res.append(b[p2])
        p2 += 1
    else:
        res.append(a[p1])
        p1 += 1

if p1<aLen :
    res = res + a[p1:]
else:
    res = res + b[p2:]

for x in res:
    print(x, end=" ")
