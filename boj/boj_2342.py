from sys import stdin, maxsize, setrecursionlimit

setrecursionlimit(10**6)
input = stdin.readline

a = list(map(int, input().split()))
al = len(a)
d = [[[-1]*5 for _ in range(5)] for _ in range(al)]

plus = [
[0,2,2,2,2],
[0,1,3,4,3],
[0,3,1,3,4],
[0,4,3,1,3],
[0,3,4,3,1]]

def dfs(idx, l, r):
    if idx==al:
        return 0
    if d[idx][l][r]!=-1:
        return d[idx][l][r]
    d[idx][l][r] = maxsize
    if a[idx]!=r:
        d[idx][l][r] = min(d[idx][l][r], dfs(idx+1,a[idx],r)+plus[l][a[idx]])
    if a[idx]!=l:
        d[idx][l][r] = min(d[idx][l][r], dfs(idx+1,l,a[idx])+plus[r][a[idx]])
    return d[idx][l][r]
print(dfs(0,0,0))