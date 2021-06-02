from sys import stdin, setrecursionlimit, maxsize
from math import ceil,floor,gcd


setrecursionlimit(10**6)
input = stdin.readline

n = int(input())
a = list(map(int,input().split()))

s = [0] * (n*4)

def q(i,node,nL,nR):
    if nL==nR:
        return nL
    m = (nL+nR)//2
    if i>s[node*2]:
        i-=s[node*2]
        return q(i,node*2+1,m+1,nR)
    return q(i,node*2,nL,m)

def u(i,v,node,nL,nR):
    if i<nL or i>nR:
        return s[node]
    if nL==nR:
        s[node] += (nR-nL+1)*v
        return s[node]
    m = (nL+nR)//2
    s[node] = u(i,v,node*2,nL,m)+u(i,v,node*2+1,m+1,nR)
    return s[node]

for i in range(n):
    u(i+1,1,1,1,n)

res = [0]*n
for i in range(n-1,-1,-1):
    ret = q(i-a[i]+1,1,1,n)
    res[ret-1]=i+1
    u(ret,-1,1,1,n)
print(*res)