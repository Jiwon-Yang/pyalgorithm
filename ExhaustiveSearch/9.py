import sys
sys.stdin = open('input.txt', 'r')

def makePaskal(arr, n):
    if n == 2:
        print(arr)
        return arr
    else:
        newArr = [1]
        for i in range(len(arr)-1):
            newArr.append(arr[i] + arr[i+1])
        newArr += [1]
        return makePaskal(newArr, n-1)

def makeDfs(level, x):
    if x == n:
        arr = []
        for j in range(n):
            arr.append(b[j]*res[j])
        if sum(arr) == m:
            
        return
    else:
        for i in range(1, x+1):
            if check[i] == 0:
                check[i] = 1
                res[level] = x
                makeDfs(level+1, i)
                check[i] = 0



if __name__ == "__main__":
    n, m = map(int, input().split())
    #파스칼 이항계수 
    if n == 1:
        b = [1]
    elif n == 2:
        b = [1, 1]
    else:
        b = makePaskal([1, 1], n)
    
    #수열
    res = [0]*n
    check = [0]*(n+1)
    c = makeDfs(0)
    print([1, 2, 3] * [1, 2, 3]) 
    