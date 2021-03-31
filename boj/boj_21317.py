from sys import stdin, maxsize


input = stdin.readline
a = [[] for _ in range(13)]

for _ in range(12):
    x,y=map(int,input().split())
    a[x].append(y)
    a[y].append(x)

d = []
n = 13
for i in range(1,n):
    if len(a[i])==3:
        d.append(i)

v = [0] * (n+1)
T = 1000

def dfs(n):
    v[n] = 1
    r = 1
    for i in a[n]:
        if v[i]:
            continue
        r = max(r,dfs(i)+1)
    return r
def go(n):
    r = 0
    for i in a[n]:
        if i in d:
            r += T
        else:
            v[n] = 1
            r += dfs(i)
        # print(n,i,r)
    return r

for i in d:
    v = [0] * (n+1)
    if go(i)==1007:
        print(i)
        break