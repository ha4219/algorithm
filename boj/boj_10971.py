from sys import stdin, maxsize


input = stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[-1]*(1<<n) for _ in range(n)]

all_path = (1<<n) - 1


def tsp(cur, path):
    if path==all_path:
        return a[cur][0] if a[cur][0]>0 else maxsize
    if d[cur][path]!=-1:
        return d[cur][path]
    r = maxsize
    for i in range(1,n):
        if (path>>i)%2==1 or a[cur][i]==0:
            continue
        r = min(r, a[cur][i]+tsp(i,path|(1<<i)))
    d[cur][path] = r
    return r

print(tsp(0,1))