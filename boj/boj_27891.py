import enum
from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations

MAX = 17
MOD = 1000000007
setrecursionlimit(10**6)
input = stdin.readline


s = input().strip()
a = [
    ('NorthLondonCollegiateSchool', 'NLCS'),
    ('BranksomeHallAsia', 'BHA'),
    ('KoreaInternationalSchool', 'KIS'),
    ('StJohnsburyAcademy', 'SJA'),
]
d = {}

D = 97
N = 26

for (uni, ans) in a:
    uni = uni.lower()
    uni = uni[:10]
    # res = []
    for i in range(N):
        ret = []
        for c in uni:
            ret.append((ord(c) - 97 + i) % N + D)
        # res.append(''.join(map(chr, ret)))
        d[''.join(map(chr, ret))] = ans

def main():
    print(d[s])
    return

if __name__ == '__main__':
    main()