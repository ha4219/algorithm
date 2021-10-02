def tree_update(i,diff):
	while i<=N:
		tree[i]+=diff
		i+=i&-i
def tree_sum(i):
	r=0
	while i:
		r+=tree[i]
		i&=i-1
	return r
import sys
input=sys.stdin.readline
N=int(input())
tree=[0]*(N+5)
a=[0]*1000005
b=[0]*(N+5)
for idx,i in enumerate(map(int,input().split())):
	b[idx+1]=a[i]
	a[i]=idx+1
M=int(input())
query=[tuple(map(int,input().split()))+(i,)for i in range(M)]
query.sort(key=lambda x:x[1])
ans=[0]*M
cur=0
for i in range(1,1+N):
	if b[i]:
		tree_update(b[i],-1)
	tree_update(i,1)
	while cur<M:
		if query[cur][1]!=i:break
		ans[query[cur][2]]=tree_sum(query[cur][1])-\
            tree_sum(query[cur][0]-1)
		cur+=1
print(*ans,sep='\n')