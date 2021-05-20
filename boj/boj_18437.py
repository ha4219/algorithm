from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


input = stdin.readline
n = int(input())
lazy = [-1] * (4*n)
s = [0] * (4*n)

start = [0] * (n+1)
end = [0] * (n+1)

a = [[] for  _ in range(n+1)]
aa = list(map(int,input().split()))

for i in range(1,n):
    a[aa[i]].append(i+1)

cnt = 0
def dfs(x):
    global cnt
    cnt += 1
    start[x] = cnt
    for next in a[x]:
        dfs(next)
    end[x] = cnt

dfs(1)


def propagation(node, nL, nR):
    if lazy[node]!=-1:
        s[node] = (nR-nL+1)*lazy[node]
        if nL!=nR:
            lazy[node*2] = lazy[node]
            lazy[node*2+1] = lazy[node]
        lazy[node] = -1

def init(node, nL, nR):
    if nL==nR:
        s[node] = 1
        return s[node]
    m = (nL+nR) // 2
    s[node] = init(node*2,nL,m)+init(node*2+1,m+1,nR)
    return s[node]

def u(l,r,v,node,nL,nR):
    propagation(node, nL, nR)
    if l>nR or r<nL:
        return s[node]
    if l<=nL and nR<=r:
        lazy[node] = v
        propagation(node, nL, nR)
        return s[node]
    m = (nL+nR)//2
    s[node] = u(l,r,v,node*2,nL,m)+u(l,r,v,node*2+1,m+1,nR)
    return s[node]


def q(l,r,node,nL,nR):
    propagation(node, nL, nR)
    if l>nR or r<nL:
        return 0
    if l<=nL and nR<=r:
        return s[node]
    m = (nL+nR)//2
    return q(l,r,node*2,nL,m)+q(l,r,node*2+1,m+1,nR)

init(1,1,n)
for _ in range(int(input())):
    z,x=map(int,input().split())
    if z==1:
        if start[x]!=end[x]:
            u(start[x]+1,end[x],1,1,1,n)
    elif z==2:
        if start[x]!=end[x]:
            u(start[x]+1,end[x],0,1,1,n)
    else:
        if start[x]!=end[x]:
            print(q(start[x]+1,end[x],1,1,n))
        else:
            print(0)