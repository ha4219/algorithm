from sys import stdin


input = stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

s = []
res = 0
for i in range(n):
    while s and a[i]>=a[s[-1]]:
        s.pop()
    if s:
        res += len(s)
    s.append(i)
print(res)
