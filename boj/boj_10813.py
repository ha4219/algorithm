from sys import stdin


input = stdin.readline

n,m=map(int,input().split())
a = [i for i in range(1,n+1)]
for _ in range(m):
    p,q = map(int,input().split())
    a[p-1],a[q-1]=a[q-1],a[p-1]
print(*a)