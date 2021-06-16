from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = list(map(int,input().split()))

up = 1
res = 1

for i in range(n-1):
    if up:
        if a[i]>=a[i+1]:
            up = 0
    else:
        if a[i]<=a[i+1]:
            res = 0
            break
print('YES' if res else 'NO')