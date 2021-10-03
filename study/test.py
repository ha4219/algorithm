from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

s = input().strip()
sl = len(s)

end = -1
l = 0
def next(cidx, l, cur):
    if cur==9 and l==1 and sl>=cidx+3:
        if cur+1==int(s[cidx+1:cidx+3]):
            return (cidx+1,2,cur+1)
    if cur==99 and l==2 and sl>=cidx+5:
        if cur+1==int(s[cidx+2:cidx+5]):
            return (cidx+2, 3, cur+1)
    
    if cur+1==int(s[cidx+l:cidx+2*l]) and sl>=cidx+l*2:
        return (cidx+l, l, cur+1)
    return (-1, -1, cur)

res = 0
for i in range(1,1000):
    try:
        # print(i, int(s[0:len(str(i))]))
        if i!=int(s[0:len(str(i))]):
            continue
        start = i
        cidx, l, cur = next(0,len(str(i)),i)
        # print(cidx, l, cur)
        if cidx != -1:
            while 1:
        # print(cidx, l, cur)
                try:
                    cidx, l, cur = next(cidx, l, cur)
                except:
                    break
            if cidx+l==sl:
                start = i
                end = cur
                res = 1
    except:
        if res:
            break
        continue
    if res:
        break

if end==-1:
    print(start, start)
else:
    print(start, end)