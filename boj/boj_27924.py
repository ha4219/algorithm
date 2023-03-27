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


N = int(input())
a =[[] for _ in range(N+1)]

for _ in range(N-1):
    l, r = map(int, input().split())
    a[l].append(r)
    a[r].append(l)

qs = list(map(int, input().split()))

def main():
    # ( pos, isYun )
    q = deque([(qs[1], 2), (qs[2], 2), (qs[0], 1)])
    v = [0] * (N + 1)
    v[qs[0]] = 1;v[qs[1]] = 2;v[qs[2]] = 2
    while q:
        pos, is_yun = q.popleft()
        if is_yun == 1 and len(a[pos]) == 1:
            print('YES');return;
        for nn in a[pos]:
            if not v[nn]:
                v[nn] = is_yun
                q.append((nn, is_yun))
    print('NO');return;
    


if __name__ == '__main__':
    main()