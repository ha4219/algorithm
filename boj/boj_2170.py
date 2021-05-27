from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**6)
input = stdin.readline

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

a.sort()

res = 0
l = -maxsize
r = -maxsize
for i in range(n):
    if r<a[i][0]:
        res += r-l
        l = a[i][0]
        r = a[i][1]
    else:
        r = max(r,a[i][1])
res += r-l
print(res)