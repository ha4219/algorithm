from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations, permutations
import math


MAX = 17
MOD = 1000000007
setrecursionlimit(10**6)
input = stdin.readline

s = input().strip()
a = [0] * 26

def main():
    for c in s:
        a[ord(c)-ord('A')] += 1
    res = 1
    for c in 'MOBIS':
        res *= a[ord(c)-ord('A')]
    print('YES' if res else 'NO')
    return


if __name__ == "__main__":
    main()
