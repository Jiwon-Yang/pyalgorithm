# 자료형
Single
* Integer
* Float
* String
* Boolean

Container
* List
* Tuple
* Dictionary
* Set


# 논리연산
* short circuit 
	* or : 앞 항이 참이면 참
	* and : 앞 항이 거짓이면 거짓


# 연산자
```
+
-
*
/ 
// : 몫
% : 나머지
** : 거듭제곱
```

1//3
Immutable 변수 : 리스트 활용


# 조건문
```
if 조건문:
    결과1
elif 조건문:
    결과2
else:
    결과3
```


# 반복문
```
for i in range(1, 10):
    if 조건문:
        continue // 뒤에 코드 실행하지 않음
    elif 조건문:
        break   // 반복문을 빠져나감
    print('a')
```
```
while 조건문:
    결과
```


# 문자열
```
msg = 'hello world!'
msg.upper()     # 대문자화
msg.lower()     # 소문자화
msg.find('e')      # 처음으로 발견되는 인덱스 출력
msg.count('e')      # 갯수
msg[:2]     # slice
len(msg)    # 길이
```

```
isupper()
islower()
isalpha()

msg = 'Hello World!'
for x in msg:
    if x.isupper():
        print(x)    # H W
```

```
# ord, chr
# A : 65, a : 97
# Z : 90, z : 122

ascii_A = 'A' 
print(ord(ascii_A))     # 65
ascii_65 = 65
print(chr(ascii_65))    # A
```

```
# enumerate
a = [10, 20, 30]
for i in enumerate(a):
    print(i)
# 인덱스 포함한 튜플 반환
# (0, 10)
# (1, 20)
# (2, 30)

for i in enumerate(a):
    print(i[0], i[1])

for idx, val in enumerate(a):
    print(idx, val)
```

```
# all, any
a = [10, 20, 30]

# all : 모두 참이어야 참
if (40>x for x in a):
    print("Y")
else:
    print("N")

# any : 하나라도 참이면 참
if (15>x for x in a):
    print("Y")
else:
    print("N")
```


# 리스트
```
a = list(range(0, 6))
a.append(7)
a.insert(3, 7)
a.pop(3)        # 인덱스 찾아서 제거
a.remove(4)     # 값 찾아서 제거
a.index(5)      # 값의 인덱스
```
```
sum(a)
max(a)      # 인자 값들 중 최댓값 출력
min(a)
```

```
import random as r
r.shuffle(a)            # 무작위 섞기
a.sort()                # 오름차순
a.sort(reverse=True)    # 내림차순
a.clear()
```


# 2차원 리스트
```
a = [0] * 3
b = [[0]*3 for _ in range(3)]
```

```
# 좌표 접근
a = [[0, 1, 3], [4, 5, 6], [7, 8, 9]]

for x in a:
    print(x)
# [0, 1, 3] 
# [4, 5, 6]
# [7, 8, 9]

for x in a:
    for y in x:
        print(y, end=' ') 
    print() # 줄바꿈
# 0 1 3 
# 4 5 6
# 7 8 9
```


# 값 교환
```
a, b = 10, 20
a, b = b , a
```


# 입력받기
```
a, b = map(int, input().split(" "))
```


# 출력하기
```
print(a, b, c, sep=', ') # a, b, c
','.join(['a', 'b', 'c']) // a, b, c
```


# 함수
```
def plus_one(x):
    return x+1

print(plus_one(1))
```


# 람다 함수
```
plus_two = lamda x: x+2
print(plus_two(2))
```

```
a = [1, 2, 3]
print(list(map(lamda x: x+2, a)))
```