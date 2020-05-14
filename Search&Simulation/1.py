# 회문 문자열 검사

tc = int(input())

for i in range(tc):
    word = input()
    word = word.upper() # 대소문자 구분 없애기 주의
    wordLen = len(word)
    for j in range(wordLen//2):
        if word[j]!=word[wordLen-1-j] :
            print('#%d NO' % (j+1))
            break
    else:
        print('#%d YES' % (j+1))
