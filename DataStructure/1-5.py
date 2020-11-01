n=int(input())
stack=[]
print_list=[]
i=1
 
 
while(n>0):
    n -= 1
    sequence=int(input())
    if len(stack)==0:
        stack.append(i)
        print_list.append("+")
        i += 1
 
    while(stack[len(stack)-1]<sequence):
        stack.append(i)
        print_list.append("+")
        i += 1
    if stack[len(stack)-1]==sequence:
        stack.pop()
        print_list.append("-")
    elif stack[len(stack) - 1] > sequence:
        print_list = []
        print_list.append("NO")
        break
 
 
 
for i in print_list:
    print(i)