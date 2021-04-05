from sys import stdin


n,m=map(int,input().split())
s = set()
for _ in range(n):
    s.add(input().strip())
res = 0
for _ in range(m):
    if input().strip() in s:
        res += 1
print(res)