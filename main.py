from sys import stdin, setrecursionlimit, maxsize
from math import gcd


input = stdin.readline
setrecursionlimit(10**6)
MAX = 100002
class Node:
    def __init__(self,l=0,r=0,v=0):
        self.l = l
        self.r = r
        self.v = v


def init(nn,nL,nR):
    if nL==nR:
        return
    m = (nL+nR)//2
    node.append(Node())
    node[nn].l = len(node)-1
    init(node[nn].l,nL,m)
    node.append(Node())
    node[nn].r = len(node)-1
    init(node[nn].r,m+1,nR)

def u(i,x,nn,nL,nR):
    if nL==nR:
        return
    m = (nL+nR)//2
    if i<=m:
        ln = node[nn].l
        node.append(Node(node[ln].l,node[ln].r,node[ln].v+x))
        node[nn].l = len(node)-1
        u(i,x,node[nn].l,nL,m)
    else:
        rn = node[nn].r
        node.append(Node(node[rn].l,node[rn].r,node[rn].v+x))
        node[nn].r=len(node)-1
        u(i,x,node[nn].r,m+1,nR)

def q(l,r,nn,nL,nR):
    if r<nL or l>nR:
        return 0
    if l<=nL and nR<=r:
        return node[nn].v
    m = (nL+nR)//2
    return q(l,r,node[nn].l,nL,m)+q(l,r,node[nn].r,m+1,nR)

for __ in range(int(input())):
    n,m=map(int,input().split())
    head = [0] * MAX
    node = [0, Node()]
    head[0] = 1
    init(1,1,MAX)
    yidx = [[] for _ in range(MAX)]
    for _ in range(n):
        x,y=map(int,input().split())
        x += 1;y+=1
        yidx[x].append(y)
    for i in range(1,MAX):
        if head[i]==0:
            node.append(Node(node[head[i-1]].l,node[head[i-1]].r,node[head[i-1]].v))
            head[i] = len(node) - 1
        for y in yidx[i]:
            node[head[i]].v += 1
            u(y,1,head[i],1,MAX)
    res = 0
    for _ in range(m):
        l,r,b,t=map(int,input().split())
        res += q(b+1,t+1,head[r+1],1,MAX)-q(b+1,t+1,head[l],1,MAX)
    print(res)