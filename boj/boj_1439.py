from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 200000
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

'''
1
6 9

2 
6 9

3
4 6 7 8 9 10

4 x

5
6 9

6 x
9

7 x
8 9

8 x
9 10

9 x

10 x

3 seg ?

'''

s = input().strip()
sl = len(s)
cnt0 = 0
cnt1 = 0
prev = s[0]
for i in range(1, sl):
    if s[i-1] == '0' and s[i] == '1':
        cnt0 += 1
    elif s[i-1] == '1' and s[i] == '0':
        cnt1 += 1

print(max(cnt0, cnt1))
