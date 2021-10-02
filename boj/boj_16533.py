from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

# class DisjointSet:
#     def __init__(self, n):
#         self.data = list(range(n))
#         self.size = n

#     def find(self, index):
#         return self.data[index]

#     def union(self, x, y):
#         x, y = self.find(x), self.find(y)
#         if x==y:
#             return
#         for i in range(self.size):
#             if self.find(i) == y:
#                 self.data[i] = x

#     @property
#     def length(self):
#         return len(set(self.data))

# n, c = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(n)]

# selected = []

# def kruskal(v):
#     ret = 0
#     s = DisjointSet(v+1)
#     a.sort(key=lambda x:x[2])
#     for u,v,cost in a:  
#         if s.find(u)==s.find(v):
#             continue
#         s.union(u,v)
#         selected.append((u,v))
#         ret += cost
#     return ret

n = int(input())
a = list(map(int, input().split()))
res = 0

for i in range(1, n):
    if(a[i]>a[i-1]):
        res += 1
print(res+1)