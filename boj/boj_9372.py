from sys import stdin


input = stdin.readline

class DisjointSet:
    def __init__(self, n):
        self.data = list(range(n))
        self.size = n
    def find(self,index):
        return self.data[index]
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x==y:
            return
        for i in range(self.size):
            if self.find(i)==y:
                self.data[i]=x
    @property
    def length(self):
        return len(set(self.data))

def kruskal(v):
    ret = 0
    s = DisjointSet(v+1)
    # a.sort()
    for u,v in a:
        if s.find(u)==s.find(v):
            continue
        s.union(u,v)
        selected.append((u,v))
        ret += 1
    return ret

for _ in range(int(input())):
    n,m=map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(m)]
    # for _ in range(m):
    #     p,q=map(int,input().split())
    #     a[p-1].append(q-1)
    #     a[q-1].append(p-1)
    selected = []
    print(kruskal(n+1))