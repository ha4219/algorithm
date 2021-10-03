from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n,m = map(int,input().split())
a = list(map(int, input().split()))

# q = deque(a)
c = 0

for _ in range(m):
    s = input().split()
    if s[0]=='1':
        p,q,r = map(int, s)
        a[(c+q-1+n)%n] += r
    else:
        p,q = map(int, s)
        if p==2:
            c = (c+q)%n
        else:
            c = (c+n-q)%n
    print(c)
    print(a)
        
print(*a[c:],end=' ')
print(*a[:c])
