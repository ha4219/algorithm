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

n = int(input())

a = list(map(int, input().split()))
res = 0
for v in a:
    res = 1 - (1-res)*(1-v/100)
    print(res * 100)
