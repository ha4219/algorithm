from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**6)
input = stdin.readline

n = int(input())
a = list(map(int,input().split()))

s = []
res = []
for i in range(n-1,-1,-1):
    while len(s) and s[-1]<=a[i]:
        s.pop()
    if len(s):
        res.append(s[-1])
    else:
        res.append(-1)
    s.append(a[i])
print(*reversed(res))