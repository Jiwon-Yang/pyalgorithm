import sys
sys.setrecursionlimit(10**9)
 
n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))#중위순회
postorder = list(map(int, sys.stdin.readline().split()))#후위순회
in_location=[0 for _ in range(n+1)]
for i in range(n):
    in_location[inorder[i]]=i
 
tree=[[0,0] for _ in range(n+1)]
 
def find_tree(in_l,in_r,post_l,post_r):
    if post_l <= post_r:
        parents=postorder[post_r]
        p_index=in_location[parents]
 
        l_count=p_index-in_l
        if l_count>0:
            tree[parents][0]=postorder[post_l+l_count-1]
        r_count=in_r-p_index
        if r_count>0:
            tree[parents][1]=postorder[post_r-1]
 
 
        find_tree(in_l , p_index-1 , post_l , post_l+l_count-1)
        find_tree(p_index+1 , in_r , post_r-r_count , post_r-1)
 
find_tree(0,n-1,0,n-1)
 
def pre_order(start):
    print(start,end=" ")
    if tree[start][0] != 0:
        pre_order(tree[start][0])
    if tree[start][1] != 0:
        pre_order(tree[start][1])
 
pre_order(postorder[-1])