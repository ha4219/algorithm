from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 100001
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

a1, a0 = map(int, input().split())
c1, c2 = map(int, input().split())
n0 = int(input())

left = c1 * n0
center = a1 * n0 + a0
right = c2 * n0

print(1 if left <= center <= right and c1 <= a1 <= c2  else 0)