from sys import stdin


input = stdin.readline

n, m = map(int,input().split())
lazy = [0] + [0] * (n*4)
s = [0] + [0] * (n*4)

def propagation(node, nL, nR):
    # print(node, nL, nR)
    if lazy[node]:
        s[node] = (nR-nL+1)-s[node]
        if nL!=nR:
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1
        lazy[node] = 0

def update(l, r, v, node, nL, nR):
    propagation(node, nL, nR)
    if l > nR or r < nL:
        return 
    if l<=nL and nR<=r:
        lazy[node] ^= 1
        propagation(node,nL,nR)
        return s[node]
    m = (nL + nR)//2
    update(l,r,v,node*2,nL,m)
    update(l,r,v,node*2+1,m+1,nR)
    s[node] = s[node*2] + s[node*2+1]
    return s[node]

def merge(l, r, node, nL, nR):
    propagation(node, nL, nR)
    if l > nR or r < nL:
        return 0
    if l <= nL and nR <= r:
        return s[node]
    m = (nL + nR)//2
    return merge(l,r,node*2,nL,m) + merge(l,r,node*2+1,m+1,nR)
    

for _ in range(m):
    t = list(map(int,input().split()))
    if t[0]==0:
        update(t[1]-1,t[2]-1,1,1,0,n-1)
    else:
        print(merge(t[1]-1,t[2]-1,1,0,n-1))
    

