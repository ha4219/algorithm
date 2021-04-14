from sys import stdin


input = stdin.readline

n = int(input())

res = 0

for i in range(1,n+1):
    for j in range(i,n+1):
        if i*j<=n:
            res += 1
print(res)