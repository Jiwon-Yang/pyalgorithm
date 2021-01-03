def DFS(x):
    if x > 7:
        return
    else:
        # print(x, end=' ')
        DFS(x*2)
        # print(x, end=' ')
        DFS(x*2+1)
        print(x, end=' ')

if __name__ == "__main__":
    DFS(1)


