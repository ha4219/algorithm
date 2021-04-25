from sys import stdin


input = stdin.readline

a=list(map(int,input().split()))

d = [0] * 101
for _ in range(3):
    p,q=map(int,input().split())
    for i in range(p,q):
        d[i] += 1

res = 0
for i in range(101):
    if d[i]==0:
        continue
    res += a[d[i]-1]*d[i]
print(res)