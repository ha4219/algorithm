from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from math import exp, gcd


input = stdin.readline
setrecursionlimit(10**9)

eps = 1e-9
scale = 1e+6

def expectedRaces(c,m,p,v):
    res = p/scale
    if c>0:
        if c>v:
            if m>0:
                res += (c/scale)*(1+expectedRaces(c-v,m+v//2,p+v//2,v))
            else:
                res += (c/scale)*(1+expectedRaces(c-v,0,p+v,v))
        else:
            if m>0:
                res += (c/scale)*(1+expectedRaces(0,m+c//2,p+c//2,v))
            else:
                res += (c/scale)*(1+expectedRaces(0,0,p+c,v))
    if(m>0):
        if m>v:
            if c>0:
                res += (m/scale)*(1+expectedRaces(c+v//2,m-v,p+v//2,v))
            else:
                res += (m/scale)*(1+expectedRaces(0,m-v,p+v,v))
        else:
            if c>0:
                res += (m/scale)*(1+expectedRaces(c+m//2,m-v,p+m//2,v))
            else:
                res += (m/scale)*(1+expectedRaces(0,0,p+m,v))
    return res


for _ in range(int(input())):
    cd,md,pd,vd = map(float,input().split())
    c = round(cd*scale)
    m = round(md*scale)
    p = round(pd*scale)
    v = round(vd*scale)
    res = expectedRaces(c,m,p,v)
    print('%.12f' % res)
