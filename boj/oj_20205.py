from sys import stdin, setrecursionlimit, maxsize

input = stdin.readline
setrecursionlimit(10**6)
n,m=map(int,input().split())
MAX = n*m
res = [[0] * MAX for _ in range(MAX)]

a = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(m):
            for kk in range(m):
                res[i*m+k][j*m+kk] = a[i][j]
for i in range(MAX):
    print(*res[i])