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

N = int(input())
# A = list(map(int, input().split()))

# odd - odd = even
# even - even = even
# odd - even = odd
# evenv - odd = odd

def main():
    print(f"{' '.join(['long'] * (N // 4))} int")

if __name__ == '__main__':
    main()