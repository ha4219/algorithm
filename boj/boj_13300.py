from sys import stdin


input = stdin.readline


n,k=map(int,input().split())
a = [[0]*2 for _ in range(7)]

for _ in range(n):
    p,q=map(int,input().split())
    a[q][p] += 1
res = 0
for i in range(2):
    for j in range(1,7):
        res += a[j][i]//k if a[j][i]%k==0 else a[j][i]//k+1
print(res)