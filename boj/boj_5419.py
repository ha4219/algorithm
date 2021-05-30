from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**6)
input = stdin.readline
MAX = 75001

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
    a = [list(map(int,input().split())) for _ in range(n)]
    s = [0] * (n+1)

    a.sort(key=lambda x: (x[1],-x[0]))
    for i in range(n):
        a[i][1] = i+1
    a.sort(key=lambda x: (-x[0],x[1]))

    res = 0
    for i in range(n):
        res += q(a[i][1])
        u(a[i][1],1)
    print(res)