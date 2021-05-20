from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


input = stdin.readline
n,m=map(int,input().split())
aa = list(map(int,input().split()))
a = [[] for _ in range(n+1)]
for i in range(1,n):
    a[aa[i]].append(i+1)

s = [0] * (4*n)
lazy = [0] * (4*n)
start = [0]*(n+1)
end = [0]*(n+1)

def propagation(node, nL, nR):
    if lazy[node]:
        s[node] += (nR-nL+1)*lazy[node]
        if nL!=nR:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def init(node, nL, nR):
    if nL==nR:
        s[node] = aa[nL]
        return s[node]
    m = (nL+nR)//2
    s[node] = init(node*2,nL,m)+init(node*2+1,m+1,nR)
    return s[node]

def u(l,r,v,node,nL,nR):
    propagation(node, nL, nR)
    if nL>r or nR<l:
        return s[node]
    if l<=nL and nR<=r:
        lazy[node] += v
        propagation(node, nL, nR)
        return s[node]
    m = (nL+nR)//2
    s[node]=u(l,r,v,node*2,nL,m)+u(l,r,v,node*2+1,m+1,nR)
    return s[node]


def q(l,r,node,nL,nR):
    propagation(node, nL, nR)
    if nL>r or nR<l:
        return 0
    if nL==nR:
        return s[node]
    m = (nL+nR)//2
    return q(l,r,node*2,nL,m)+q(l,r,node*2+1,m+1,nR)


cnt = 0
def dfs(x,par):
    global cnt
    cnt += 1
    start[x] = cnt
    for next in a[x]:
        if next==par:
            continue
        dfs(next,x)
    end[x] = cnt
dfs(1,-1)
for _ in range(m):
    t = list(map(int,input().split()))
    if t[0] == 1:
        u(start[t[1]],start[t[1]],t[2],1,1,n)
    else:
        print(q(start[t[1]],end[t[1]],1,1,n))