from sys import stdin


input = stdin.readline

n,q1,q2 = map(int,input().split())
a = list(map(int,input().split()))
lazy = [0] + [0] * (n*4)
s = [0] + [0] * (n*4)

def propagation(node, nL, nR):
    if lazy[node]:
        s[node] += (nR-nL+1) * lazy[node]
        if nL!=nR:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def init(node, nL, nR):
    if nL==nR:
        s[node] = a[nL]
        return s[node]
    m = (nL+nR)//2
    s[node] = init(node*2,nL,m) + init(node*2+1,m+1,nR)
    return s[node]

def update(l, r, v, node, nL, nR):
    propagation(node, nL, nR)
    if l > nR or r < nL:
        return 
    if l<=nL and nR<=r:
        lazy[node] += v
        if nL!=nR:
            lazy[node*2]+=v
            lazy[node*2+1]+=v
        return 
    m = (nL + nR)//2
    update(l,r,v,node*2,nL,m)
    update(l,r,v,node*2+1,m+1,nR)
    s[node] = s[node*2] + s[node*2+1]
    return 

def merge(l, r, node, nL, nR):
    propagation(node, nL, nR)
    if l > nR or r < nL:
        return 0
    if l <= nL and nR <= r:
        return s[node]
    m = (nL + nR)//2
    return merge(l,r,node*2,nL,m) + merge(l,r,node*2+1,m+1,nR)

init(1,0,n-1)

for _ in range(q1+q2):
    t = list(map(int,input().split()))
    if t[0]==2:
        update(t[1]-1,t[2]-1,t[3],1,0,n-1)
    else:
        print(merge(t[1]-1,t[2]-1,1,0,n-1))
