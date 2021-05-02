from sys import stdin


input = stdin.readline



def update(i, val, node, l, r):
    if r<i or l>i:
        return s[node]
    if l==r:
        s[node] = val
        return val
    m = (l+r)//2
    s[node] = update(i, val, node*2, l, m) + update(i, val, node*2+1, m+1, r)
    return s[node]

def q(x, y, node, l, r):
    if l>y or r<x:
        return 0
    if x<=l and r<=y:
        return s[node]
    m = (l+r)//2
    return q(x,y,node*2,l,m)+q(x,y,node*2+1,m+1,r)


for _ in range(int(input())):
    n,m=map(int,input().split())
    s = [0] * (4*(n+m))
    a = [0]
    for i in range(n):
        a.append(m+i)
        update(m+i,1,1,0,n+m)
    t = m
    query = list(map(int,input().split()))
    res = []
    for i in range(m):
        res.append(q(t,a[query[i]],1,0,n+m)-1)
        update(a[query[i]],0,1,0,n+m)
        t -= 1
        a[query[i]] = t
        update(t,1,1,0,n+m)
    print(*res)