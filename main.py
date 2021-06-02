from sys import stdin, setrecursionlimit, maxsize
from math import ceil,floor,gcd



setrecursionlimit(10**6)
input = stdin.readline

def q(i):
    res = 0
    while i>0:
        res += s[i]
        i &= (i-1)
    return res

def u(i,v):
    while i<n+1:
        s[i] += v
        i += (i&-i)

for _ in range(int(input())):
    n = int(input())
    t = list(map(int,input().split()))
    k = [0] * (n+1)
    a = [0] * n
    for i in range(n):
        k[t[i]] = i
    t = list(map(int,input().split()))
    for i in range(n):
        a[k[t[i]]] = i+1

    s = [0] * (n+1)

    res = 0
    for i in range(n):
        t = a[i]
        p = q(n)-q(t)
        res += p
        u(t,1)
    print(res)