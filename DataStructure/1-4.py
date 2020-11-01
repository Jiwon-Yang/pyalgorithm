import sys
 
class Stack:
    def __init__(self):
        self.len = 0
        self.list = []
 
    def pop(self):
        pop_result=self.list[self.len-1]
        del self.list[self.len-1]
        self.len -= 1
        return pop_result
 
    def push(self,num):
        self.len += 1
        self.list.append(num)
 
 
n=int(input())
stack=Stack()
sum=0
while(n>0):
    n-=1
    command=sys.stdin.readline().split()
    if command[0]=='0':
        stack.pop()
    else:
        stack.push(command[0])
 
 
for i in stack.list:
    sum+=int(i)
 
 
print(sum)