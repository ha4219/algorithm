from sys import stdin, setrecursionlimit, maxsize
from collections import deque


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = list(map(int,input().split()))
d=[[1 if i==j else 0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n-i):
        if i==0:
            d[j][j]=1
        elif i==1:
            d[j][j+1]=(1 if a[j]==a[j+1] else 0)
        else:
            d[j][i+j]=(d[j+1][j+i-1] if a[j]==a[j+i] else 0)

res = -1
def f(i, c):
    if i==n:
        global res
        res = max(res,c)
        print(res)
        exit(0)
    else:
        for next in range(i+1,n,2):
            if d[i][next]:
                f(next+1,c+1)
for i in d:
    print(*i)
f(0,0)
print(res)

