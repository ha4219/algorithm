from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**6)
input = stdin.readline

n, m = map(int,input().split())
a = []

for _ in range(n):
    p,q=map(int,input().split())
    if p>q:
        a.append((q,p))

l=r=0
a.sort()
res = 0
for i in range(len(a)):
    if r<=a[i][0]:
        res += (r-l)*2
        l = a[i][0]
        r = a[i][1]
    else:
        r = max(r,a[i][1])
res += (r-l)*2
print(res+m)