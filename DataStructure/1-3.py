import sys
 
n=int(input())
 
while(n>0):
    n-=1
    vps=sys.stdin.readline().strip()
    stack_len = 0
    for i in vps:
        if i=='(':
            stack_len+=1
        elif i==')':
            stack_len-=1
        if stack_len<0:
            print("NO")
            break
 
    if stack_len==0:        
        print("YES")
    elif stack_len>0:
        print("NO")
