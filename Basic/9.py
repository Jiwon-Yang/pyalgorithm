# 주사위 게임

tc = int(input())
res = 0

for i in range(tc):
    money = 0
    arr = list(map(int, input().split()))
    arr.sort()
    a, b, c = map(int, arr)

    if a==b and b==c:
        money = 10000 + c*1000
    elif a==b or b==c:
        money = 1000 + b*100
    else:
        money = c*100
    
    if money>res:
        res = money
     

print(res)
    

            