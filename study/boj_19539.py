from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt


input = stdin.readline
setrecursionlimit(10**6)


def f(s, bit):
    sl = len(s)
    # print(sl, s)
    if sl==1:
        if s[0]=='0':
            return 0
        elif s[0]=='1':
            return 1
        else:
            x = bit&(1<<(ord(s[0])-ord('a')))
            return x
    idx = s.find('?')
    if(idx==-1):
        if s[0]=='0' or s[0]=='1':
            x= int(s[0])
        else:
            x = 1 if bit&(1<<(ord(s[0])-ord('a'))) else 0
        if s[3]=='0' or s[3]=='1':
            y=int(s[3])
        else:
            y = 1 if bit&(1<<(ord(s[3])-ord('a'))) else 0
        if x==y:
            return 1
        else:
            return 0
    else:
        eq = s.find(':')
        if s[0]=='0' or s[0]=='1':
            x= int(s[0])
        else:
            x = 1 if bit&(1<<(ord(s[0])-ord('a'))) else 0
        if idx==1:
            if x:
                return f(s[2:eq], bit)
            else:
                return f(s[eq+1:], bit)
        else:
            if s[3]=='0' or s[3]=='1':
                y=int(s[3])
            else:
                y = 1 if bit&(1<<(ord(s[3])-ord('a'))) else 0
            # print(x,y,idx,sl)
            if x==y:
                return f(s[5:eq], bit)
            else:
                return f(s[eq+1:], bit)

n = int(input())
s = input().strip()
MAX = 1<<n
res = 0
for i in range(MAX):
    if f(s, i)==0:
        res += 1
print(res)