from sys import stdin

input = stdin.readline

n = int(input())
a = list(map(int,input().split()))

a.sort(reverse=True)
res = -1
for i in range(n):
    res = max(res, 2+i+a[i])
print(res)
