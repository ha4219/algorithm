import enum
from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations

MAX = 17
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
lr = [0 for _ in range(N*2-1)]
rl = [0 for _ in range(N*2-1)]

get_lr_index = lambda x, y: x - y + N - 1
get_rl_index = lambda x, y: x + y  
a_odd = [(i, j) for i in range(N) for j in range(N) if A[i][j] and (i+j) % 2]
a_even = [(i, j) for i in range(N) for j in range(N) if A[i][j] and (i+j) % 2 == 0]

res = 0

# a = 100, lr = 19, 100 ^ 19? => TLE?
# a = 100, next_index, with type
def dfs(next_index, d, t):
    res = d
    a = a_odd if t else a_even
    for i, (x, y) in enumerate(a[next_index:], next_index):
        lr_i, rl_i = get_lr_index(x, y), get_rl_index(x, y)
        if lr[lr_i] == rl[rl_i] == 0:
            lr[lr_i] = 1
            rl[rl_i] = 1
            res = max(dfs(i+1, d+1, t), res)
            lr[lr_i] = 0
            rl[rl_i] = 0
    return res


def main():
    print(dfs(0, 0, 0) + dfs(0, 0, 1))

if __name__ == '__main__':
    main()