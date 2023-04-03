import enum
from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations
import math

MAX = 17
MOD = 1000000007
setrecursionlimit(10**6)
input = stdin.readline

N, M = map(int, input().split())
s = input().strip()

# dist list create  O(n) 어케하냐 ㅋㅋ
# dist 로 sort O(nlogn)
# m 번 반복?
# 재구성 O(n)

def main():
    d = [] # [(dist: 이전 X와의 거리, index)]
    l = 0
    t = 0
    for i, c in enumerate(s, 1):
        if c=='.':
            d.append((i - l, i))
            t += 1
        else:
            l = i
            d.append((maxsize, i))
    if l == 0: # X가 없음.
        print(N)
        return
    d = sorted(d, key=lambda x:x[0])
    m = M
    ret = [] # (dist, index, is_dot)
    for (dist, i) in d:
        tmp = dist
        is_dot = dist != maxsize
        if dist <= m:
            m -= dist
            tmp = maxsize
        ret.append((tmp, i, is_dot))
    ret = sorted(ret, key=lambda x:x[1])
    res = 0
    i = 0
    while i < N:
        d, idx, is_dot = ret[i]
        print(d, idx, is_dot)
        if not is_dot:
            for j in range(idx+1, N):
                if ret[j-1][0] == maxsize:
                    break
            i = j
            res += 2
            continue
        res += 1
        i += 1


    print(res)

    return

if __name__ == '__main__':
    main()