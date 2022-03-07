from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 100001
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

left = a1 * n0 + a0
right = c * n0

print(1 if left >= right and a1 >= c  else 0)