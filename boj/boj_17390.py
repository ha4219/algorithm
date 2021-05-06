from sys import stdin

input = stdin.readline

n, q = map(int,input().split())
a = list(map(int, input().split()))
a.sort()
d = [0] * n

for i in range(n):
    if i==0:
        d[i] = a[i]
    else:
        d[i] = d[i-1] + a[i]

for _ in range(q):
    l,r = map(int,input().split())
    if l==1:
        print(d[r-1])
    else:
        print(d[r-1]-d[l-2])
