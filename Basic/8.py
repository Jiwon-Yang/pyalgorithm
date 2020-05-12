# 뒤집은 소수
# 다시 풀어보기!

def reverse(x):
    res = 0
    while x>0:
        num = x % 10
        x = x // 10
        res = res*10 + num
    return res


def isPrime(x):
    if x == 1: # 1인 경우 예외 처리 주의
        return False
    for i in range(2, x//2): # x//2 까지만 해도 됨
        if(x%i==0):
            return False
    return True


n = int(input())
arr = list(map(int, input().split()))

for x in arr:
    rev = reverse(x)
    if isPrime(rev):
        print(rev, end=' ')
    