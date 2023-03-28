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


N = int(input())
a =[input().strip() for _ in range(N)]

def main():
    l = r = 0
    for i in a:
        if i == 'D':
            l += 1
        else:
            r += 1
        if abs(l-r)>=2:
            break
    print(f'{l}:{r}')

if __name__ == '__main__':
    main()