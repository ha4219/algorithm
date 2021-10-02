from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

st = input().strip()

d = {
    'A':3,
    'B':2,
    'C':1,
    'D':2,
    'E':3,
    'F':3,
    'G':3,
    'H':3,
    'I':1,
    'J':1,
    'K':3,
    'L':1,
    'M':3,
    'N':3,
    'O':1,
    'P':2,
    'Q':2,
    'R':2,
    'S':1,
    'T':2,
    'U':1,
    'V':1,
    'W':2,
    'X':2,
    'Y':2,
    'Z':1,
}

a = []
n = len(st)
s = [0] * (n*4)
for c in st:
    a.append(d[c])

def init(node, nL, nR):
    if nL==nR:
        s[node] = a[nL]
        return s[node]
    m = (nL+nR)//2
    s[node] = (init(node*2,nL,m)+init(node*2+1,m+1,nR))%10
    return s[node]
res = init(1, 0, n-1)
print("I'm a winner!" if res&1 else "You're the winner?")