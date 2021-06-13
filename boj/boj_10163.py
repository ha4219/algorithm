from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

MAX = 102
a = [[0]*MAX for _ in range(MAX)]

n = int(input())
for i in range(1,n+1):
    x1,y1,w,h=map(int,input().split())
    for x in range(x1,x1+w):
        for y in range(y1,y1+h):
            a[x][y] = i

res = [0] * (n)
for i in range(MAX):
    for j in range(MAX):
        if a[i][j]:
            res[a[i][j]-1] += 1
print('\n'.join(map(str, res)))
