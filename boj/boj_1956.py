from sys import stdin,maxsize


input = stdin.readline

n,m=map(int,input().split())
d = [[maxsize]*n for _ in range(n)]
for _ in range(m):
    p,q,r=map(int,input().split())
    d[p-1][q-1] = r


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                d[i][j]=0
            else:
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])

res = maxsize

for i in range(n):
    for j in range(n):
        if i==j or d[i][j]==maxsize or d[j][i]==maxsize:
            continue
        res = min(res,d[i][j]+d[j][i])
print(res if res!=maxsize else -1)