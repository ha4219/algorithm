from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline

n = int(input())
sqrtN = int(sqrt(n))

cnt = [0] * (1000001)

def add(idx):
    global res
    if cnt[a[idx]]==0:
        res += 1
    cnt[a[idx]] += 1

def erase(idx):
    global res
    cnt[a[idx]] -= 1
    if cnt[a[idx]]==0:
        res -= 1

a = [0] + list(map(int,input().split()))
q = int(input())
query = []
order = []

for i in range(q):
    s, e = map(int, input().split())
    query.append((i, s, e))
    order.append((s/sqrtN,e,i))

order.sort()

s, e= query[0][1], query[0][2]
# print('s e',s, e)
res = 0
ret = [0] * q
for i in range(s,e+1):
    add(i)

ret[query[0][0]] = res
for i in range(1, q):
    idx = order[i][2]
    # print('start', s, e)
    # print(cnt[:4])
    while s<query[idx][1]:
        # res -= a[s]
        erase(s)
        s += 1
    while s>query[idx][1]:
        s -= 1
        # res += a[s]
        add(s)
    while e<query[idx][2]:
        e += 1
        # res += a[e]
        add(e)
    while e>query[idx][2]:
        # res -= a[e]
        erase(e)
        e -= 1
    # print('end', s, e)
    # print(cnt[:4])
    ret[idx] = res
for i in ret:
    print(i)