from sys import stdin


input = stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
v = [0] * 100001
res = 0
prev = -1
while a:
    x = a.pop()
    if prev>=x:
        continue
    res += 1
    prev = max(prev,x)
print(res)