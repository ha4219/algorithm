from sys import stdin, maxsize, setrecursionlimit

setrecursionlimit(10**5)
input = stdin.readline

n = int(input())
m = int(input())

a = [[] for _ in range(n+1)]
for _ in range(m):
    cur, next = map(int, input().split())
    a[cur].append(next)
    a[next].append(cur)


v = [0] * (n+1)
def dfs(cur):
    res = 1
    v[cur] = 1
    for next in a[cur]:
        if v[next]: continue
        v[next] = 1
        res += dfs(next)
    return res

print(dfs(1)-1)