from sys import stdin, maxsize, setrecursionlimit


setrecursionlimit(10**6)
input = stdin.readline

n, m = map(int,input().split())
a = [0] + list(map(int,input().split()))

d = [[[-1]*(m+1) for __ in range(100)] for _ in range(n+1)]

def dfs(i,cm, mon):
    if i==n:
        return 0
    if d[i][cm][mon]!=-1:
        return d[i][cm][mon]
    d[i][cm][mon] = maxsize
    for j in range(mon+1):
        if a[i+1]+j>10:
            break
        # d[i][cm][mon] = min(d[i][cm][mon])
        if cm>a[i+1]+j:
            d[i][cm][mon] = min(d[i][cm][mon],
            dfs(i+1,a[i+1]+j,mon-j)+(-cm+a[i+1]+j)**2)
        else:
            d[i][cm][mon] = min(d[i][cm][mon], dfs(i+1,a[i+1]+j,mon-j))
    # print(i,mon,d[i][cm][mon])
    return d[i][cm][mon]

print(dfs(0, 0, m))