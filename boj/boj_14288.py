from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


input = stdin.readline
n,m=map(int,input().split())
aa = list(map(int,input().split()))
a = [[] for _ in range(n+1)]
hi = 0

for i in range(1,n):
    a[aa[i]].append(i+1)

s1 = [0] * (4*n)
lazy1 = [0] * (4*n)
s2 = [0] * (4*n)
lazy2 = [0] * (4*n)
start = [0]*(n+1)
end = [0]*(n+1)

def propagation(type, node, nL, nR):
    if type==0:
        if lazy1[node]:
            s1[node] += (nR-nL+1)*lazy1[node]
            if nL!=nR:
                lazy1[node*2] += lazy1[node]
                lazy1[node*2+1] += lazy1[node]
            lazy1[node] = 0
    else:
        if lazy2[node]:
            s2[node] += (nR-nL+1)*lazy2[node]
            if nL!=nR:
                lazy2[node*2] += lazy2[node]
                lazy2[node*2+1] += lazy2[node]
            lazy2[node] = 0


def u(type,l,r,v,node,nL,nR):
    if type==0:
        propagation(type,node, nL, nR)
        if nL>r or nR<l:
            return s1[node]
        if l<=nL and nR<=r:
            lazy1[node] += v
            propagation(type,node, nL, nR)
            return s1[node]
        m = (nL+nR)//2
        s1[node]=u(type,l,r,v,node*2,nL,m)+u(type,l,r,v,node*2+1,m+1,nR)
        return s1[node]
    else:
        if nL>r or nR<l:
            return s1[node]
        if l<=nL and nR<=r:
            lazy2[node] += v
            propagation(type,node, nL, nR)
            return s2[node]
        m = (nL+nR)//2
        s2[node]=u(type,l,r,v,node*2,nL,m)+u(type,l,r,v,node*2+1,m+1,nR)
        return s2[node]


def q(type,l,r,node,nL,nR):
    if type==0:
        propagation(type,node, nL, nR)
        if nL>r or nR<l:
            return 0
        if nL==nR:
            return s1[node]
        m = (nL+nR)//2
        return q(type,l,r,node*2,nL,m)+q(type,l,r,node*2+1,m+1,nR)
    else:
        propagation(type,node, nL, nR)
        if nL>r or nR<l:
            return 0
        if nL==nR:
            return s2[node]
        m = (nL+nR)//2
        return q(type,l,r,node*2,nL,m)+q(type,l,r,node*2+1,m+1,nR)


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
        if hi==0:
            u(hi,start[t[1]],end[t[1]],t[2],1,1,n)
        else:
            u(hi,start[t[1]],start[t[1]],t[2],1,1,n)
    elif t[0]==2:
        print(q(0,start[t[1]],start[t[1]],1,1,n)+q(1,start[t[1]],end[t[1]],1,1,n))
    else:
        hi ^= 1