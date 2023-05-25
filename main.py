from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations, permutations
import math


MAX = 17
MOD = 1000000007
setrecursionlimit(10**6)
input = stdin.readline

# N, W, T, K = map(int, input().split())
# N, M, K = map(int, input().split())
# a = list(map(int, input().split()))
N, p, q, r = map(int, input().split())
s = input().strip()
v = [0] * N

def find_idxs(p: str):
    pl = len(p)
    arr = []
    for i in range(len(s)):
        if s[i:i+pl] == p and sum([v[j] for j in range(i, i+pl)]) == 0:
            arr.append(i)
        i += pl
    return arr

def fill_v(p, mm=maxsize):
    a = find_idxs(p)
    val = min(mm, len(a))
    for i in a[:val]:
        for j in range(i, i+len(p)):
            v[j] = 1
    return val

def main():
    global p, q, r
    res = 0
    vv = fill_v('SKH')
    res += vv
    vv = fill_v('SK', r)
    res += vv
    r -= vv
    vv = fill_v('KH', p)
    res += vv
    p -= vv
    vv = fill_v('SH', q)
    res += vv
    q -= vv
    print(res, v, p, q, r)
    vv = fill_v('S', min(q, r))
    res += vv
    q -= vv; r -= vv
    print(res, v, p, q, r)
    vv = fill_v('K', min(p, r))
    res += vv
    p -= vv; r -= vv
    vv = fill_v('H', min(p, q))
    res += vv
    p -= vv; q -= vv
    print(res, v, p, q, r)
    return


if __name__ == "__main__":
    main()
