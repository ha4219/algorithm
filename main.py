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
A = list(map(int, input().split()))

# odd - odd = even
# even - even = even
# odd - even = odd
# evenv - odd = odd

def main():
    odd = []; even = []
    for i, v in enumerate(A): # O(n)
        if v & 1: odd.append((v, i))
        else: even.append((v, i))
    
    odd = sorted(odd, key=lambda x:x[0]) # O(nlogn)
    even = sorted(even, key=lambda x:x[0]) # O(nlogn)

    # odd - odd
    for v, i in odd:
        idx = bisect_left(odd, v)
        

    return

if __name__ == '__main__':
    main()