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

x0, N = map(int, input().split())
d = {}

item = x0
i = 0

while item is not None:
    next_value = (item * 2) ^ 6 if (item & 1) else (item // 2) ^ 6
    new = d.get(next_value)
    if new:
        d[item] = (next_value, i)
        cycle = ((next_value, new[1]), i - new[1] + 1)
        break
    d[item] = (next_value, i)
    item = next_value
    i += 1
# print(d)
# print(d[7])
# print(cycle)

def main():
    cycle_value, cycle_start_index, cycle_cnt = cycle[0][0], cycle[0][1], cycle[1]

    if N <= cycle_start_index:
        x = x0
        for _ in range(N):
            x = d[x][0]
        print(x)
    else:
        n = N
        n -= cycle_start_index
        n %= cycle_cnt
        x = cycle_value
        # print(x, n)
        for _ in range(n):
            x = d[x][0]
        print(x)
    return

if __name__ == '__main__':
    main()