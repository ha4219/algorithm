from sys import stdin, setrecursionlimit, maxsize
from collections import deque

input = stdin.readline
setrecursionlimit(10**6)

n,x=map(int,input().split())
a = list(map(int,input().split()))

q = deque()
res = 0
ret = 0
d = 0

for i in a:
    d += i
    if len(q)==x:
        d -= q.popleft()
    q.append(i)
    if d > res:
        res = d
        ret = 1
    elif res==d:
        ret += 1
if res==0:
    print("SAD")
else:
    print(res)
    print(ret)