arr = [ list(map(int, input().split())) for _ in range(9) ]

def checkSudoku(arr):
    # 행끼리, 열끼리
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):    
            ch1[arr[i][j]] = 1
            ch2[arr[j][i]] = 1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    # 3*3 그룹끼리
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(0, 3):
                for s in range(0, 3):
                    s[arr[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True


if checkSudoku(arr):
    print("YES")
else:
    print("NO")