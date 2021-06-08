from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

n = 100001
lazy = [0] * (n*4)
s = [0] * (n*4)

def propagation(nd,nL,nR):
    if lazy[nd]:
        s[nd] += (nR-nL+1)*lazy[nd]
        if nL!=nR:
            lazy[nd*2] += lazy[nd]
            lazy[nd*2+1] += lazy[nd]
        lazy[nd] = 0

def u(l,r,v,nd,nL,nR):
    propagation(nd,nL,nR)
    if l>nR or r<nL:
        return s[nd]
    if l<=nL and nR<=r:
        lazy[nd] += v
        propagation(nd,nL,nR)
        return s[nd]
    m = (nL+nR)//2
    s[nd]=u(l,r,v,nd*2,nL,m)+u(l,r,v,nd*2+1,m+1,nR)
    return s[nd]

def q(l,r,nd,nL,nR):
    propagation(nd,nL,nR)
    if l>nR or r<nL:
        return 0
    if l<=nL and nR<=r:
        return s[nd]
    m = (nL+nR)//2
    return q(l,r,nd*2,nL,m)+q(l,r,nd*2+1,m+1,nR)

m = int(input())
for _ in range(m):
    l,r=map(int,input().split())
    ll,rr=q(l,l,1,1,n),q(r,r,1,1,n)
    print(ll+rr)
    if ll:
        u(l,l,-ll,1,1,n)
    if rr:
        u(r,r,-rr,1,1,n)
    u(l+1,r-1,1,1,1,n)
