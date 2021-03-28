from sys import stdin
from itertools import combinations


input = stdin.readline


a=list(map(int,input().split()))
o = []
e = []

for c in range(1,4):
    for cc in combinations(a,c):
        t = cc[0]
        for i in range(1,c):
            t*=cc[i]
        if t%2:
            o.append(t)
        else:
            e.append(t)

if len(o):
    o.sort(reverse=True)
    print(o[0])
else:
    e.sort(reverse=True)
    print(e[0])