from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd

input = stdin.readline
setrecursionlimit(10**5)

n = int(input())
a = [list(map(int, input().split(','))) for _ in range(n)]

def quick(data, left, right, idx):
    if left >= right:
        return
    pivot=data[left]

    l = left
    r = right
    while l <= r:
        while pivot[idx] > data[l][idx]: l = l+1
        while pivot[idx] < data[r][idx]: r = r-1
        if l <= r:
            data[l], data[r] = data[r], data[l]
            l, r = l+1, r-1

    quick(data, left, l-1, idx)
    quick(data, l, right, idx)

def dist(l, r):
    return (l[0]-r[0])**2+(l[1]-r[1])**2

def f(l, r):
    size = r-l+1
    if size==1:
        return maxsize
    elif size==2:
        return dist(a[l], a[r])
    elif size==3:
        res = maxsize
        for i in range(l, r):
            for j in range(i+1, r+1):
                res = min(res, dist(a[i], a[j]))
        return res
    
    m = (l+r)//2
    d = min(f(l, m), f(m+1, r))
    cmp_list = []
    for i in range(l, r+1):
        if (a[i][0]-a[m][0])**2<d:
            cmp_list.append(a[i])
    cmp_len = len(cmp_list)
    if cmp_len>=2:
        quick(cmp_list, 0, cmp_len-1, 1)
        for i in range(cmp_len-1):
            for j in range(i+1,cmp_len):
                if (cmp_list[i][1]-cmp_list[j][1])**2>=d: break
                d = min(d, dist(cmp_list[i],cmp_list[j]))
    return d

quick(a, 0, n-1, 0)

# print(f(0,n-1))
print('%.6f'%sqrt(f(0,n-1)))