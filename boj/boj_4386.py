from sys import stdin
from math import sqrt


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
    a.sort(key=lambda x:x[2])
    for u,v,c in a:
        if s.find(u)==s.find(v):
            continue
        s.union(u,v)
        selected.append((u,v))
        ret += c
    return ret

n=int(input())
aa = [list(map(float,input().split())) for _ in range(n)]
a=[]
for i in range(n):
    for j in range(i+1,n):
        a.append((i,j,sqrt(
        (aa[i][0]-aa[j][0])**2+(aa[i][1]-aa[j][1])**2
        )))

selected = []
print(kruskal(n+1))