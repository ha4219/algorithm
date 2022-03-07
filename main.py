# from sys import stdin, maxsize, setrecursionlimit
# from heapq import *
# from collections import deque
# import random

# MAX = 100001
# setrecursionlimit(10**5)
# input = stdin.readline

# n, r, c, t = map(int, input().split())
# a = list(map(int, input().split()))
# s = [0] * (4*n)
# qs = [list(map(int, input().split()))]

# def u(i, v, node, nL, nR):
#   if i < nL or i > nR:
#     return s[node]
#   if nL == nR:
#     s[node] = v
#     return s[node]
#   m = (nL + nR) // 2
#   s[node] = u(i, v, node*2, nL, m) + u(i, v, node*2+1, m+1, nR)
#   return s[node]

# def q(l, r, node, nL, nR):
#   if r < nL or l > nR:
#     return 0
#   if l<=nL and nR<=r:
#     return s[node]
#   m = (nL + nR) // 2
#   return q(l, r, node*2, nL, m) + q(l, r, node*2+1, m+1, nR)

# # for i, v in enumerate(a):
# #   u(i, v, 1, 0, n-1)


import sys
input = sys.stdin.readline
N,K=map(int,input().split())
MOD = 1000000007
K = min(N-K,K)
num,inv=1,1
for i in range(1,K+1):
    num = num* (N-i+1)%MOD
    inv = inv * i % MOD
print(num*pow(inv,MOD-2,MOD)%MOD)