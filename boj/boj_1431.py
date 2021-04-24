from sys import stdin
from functools import cmp_to_key


input = stdin.readline

arr = [input().strip() for _ in range(int(input()))]

def f1(a,b):
    ac = 0
    for c in a:
        if c.isdigit():
            ac+=int(c)
    bc = 0
    for c in b:
        if c.isdigit():
            bc+=int(c)
    return (ac, bc)

def f2(a,b):
    l = len(a)
    for i in range(l):
        if ord(a[i])!=ord(b[i]):
            if ord(a[i])<ord(b[i]):
                return -1
            else:
                return 1
    return 1

def cmp(a,b):
    al,bl=len(a),len(b)
    if al!=bl:
        if al<bl:
            return -1
        else:
            return 1
    ac,bc = f1(a,b)
    if ac!=bc:
        if ac<bc:
            return -1
        else:
            return 1
    return f2(a,b)

res=sorted(arr,key=cmp_to_key(cmp))
print('\n'.join(res))