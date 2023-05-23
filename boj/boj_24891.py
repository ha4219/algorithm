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

L, N = map(int, input().split())
a = [input().strip() for _ in range(N)]

def main():
    aa = sorted(a)
    p = list(permutations(aa, L))

    for pp in p:
        tmp = True
        for i in range(L):
            if not tmp: break
            for j in range(L):
                if not tmp: break
                if pp[i][j] != pp[j][i]:
                    tmp = False
        if tmp:
            for i in range(L):
                print(pp[i])
            return
    print("NONE")
    return


if __name__ == "__main__":
    main()
