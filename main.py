from sys import stdin, setrecursionlimit, maxsize
from collections import deque


input = stdin.readline
setrecursionlimit(10**6)

class DisjointSet:
  def __init__(self, n):
    self.data = list(range(n))
    self.size = n

  def find(self, index):
    if self.data[index]==index:
        return index
    self.data[index] = self.find(self.data[index])
    return self.data[index]

  def union(self, x, y):
    x, y = self.find(x), self.find(y)
    if y<x:
        self.data[y] = self.data[x]
    else:
        self.data[x] = self.data[y]

    @property
    def length(self):
      return len(set(self.data))

selected = []
def kruskal(v):
    res = 0
    s = DisjointSet(v+1)
    a.sort(key=lambda x:x[2])
    for u,v,cost in a:
        if s.find(u)==s.find(v):
            continue
        s.union(u,v)
        selected.append((u,v))
        res += cost
    return ret - res


n,m=map(int,input().split())
a = [list(map(int,input().split())) for _ in range(m)]
aa = [[] for _ in range(n+1)]
for i in range(m):
    aa[a[i][0]].append(a[i][1])
    aa[a[i][1]].append(a[i][0])
v = [0] * (n+1)
def dfs(idx):
    v[idx] = 1
    for next in aa[idx]:
        if v[next]:
            continue
        dfs(next)
dfs(1)
for i in range(1,n+1):
    if v[i]==0:
        print(-1)
        exit(0)
ret = 0
for i in range(m):
    ret += a[i][2]
print(kruskal(n))