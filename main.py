from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 17
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline


# nlogn??
def u(i, v, node, nL, nR):
    # if nL == nR:
    #     s[node] = v
    #     return s[node]
    if nL > i or i > nR:
        return
    if nL == nR:
        s_min[node] = v
        s_max[node] = v
        return
    m = (nL+nR)//2
    u(i, v, node*2, nL, m)
    u(i, v, node*2+1, m+1, nR)
    s_min[node] = min(s_min[node*2], s_min[node*2+1])
    s_max[node] = max(s_max[node*2], s_max[node*2+1])
    return


def q_min(l, r, node, nL, nR):
    if nL > r or nR < l:
        return maxsize
    if l <= nL and nR <= r:
        return s_min[node]
    m = (nL+nR)//2
    return min(q_min(l, r, node*2, nL, m), q_min(l, r, node*2+1, m+1, nR))


def q_max(l, r, node, nL, nR):
    if nL > r or nR < l:
        return -maxsize
    if l <= nL and nR <= r:
        return s_max[node]
    m = (nL+nR)//2
    return max(q_max(l, r, node*2, nL, m), q_max(l, r, node*2+1, m+1, nR))


for ____ in range(int(input())):
    n, k = map(int, input().split())

    arr = [i for i in range(n)]
    s_min = [maxsize] * (4*n)
    s_max = [maxsize] * (4*n)

    '''
    min
    max
    '''

    for i in range(n):
        u(i, i, 1, 0, n-1)

    for _ in range(k):
        a, b, c = map(int, input().split())

        if a:
            l = q_min(b, c, 1, 0, n-1)
            r = q_max(b, c, 1, 0, n-1)

            print('YES' if l == b and r == c else 'NO')
        else:
            left = arr[b]
            right = arr[c]
            u(b, right, 1, 0, n-1)
            u(c, left, 1, 0, n-1)
            arr[b], arr[c] = arr[c], arr[b]
