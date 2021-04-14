from sys import stdin


input = stdin.readline
n = int(input())

res = 0
b = 0
while b<=n:
    b += 2*res*res+res*2+1
    res += 1

print(res-1)
