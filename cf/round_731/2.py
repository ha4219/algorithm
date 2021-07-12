from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from math import gcd


input = stdin.readline
# setrecursionlimit(10**6)

def f(s):
    sl = len(s)
    l = r = s.find('a')
    c = ord('a')
    if l==-1:
        return False
    c += 1
    l -= 1
    r += 1
    while not (l==-1 and r==sl):
        if l>-1 and chr(c) == s[l]:
            c += 1
            l -= 1
        elif r<sl and chr(c) == s[r]:
            c += 1
            r += 1
        else:
            return False
    return l==-1 and r==sl

for __ in range(int(input())):
    s = input().strip()
    print('Yes' if f(s) else 'No')