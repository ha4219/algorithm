from sys import stdin,maxsize
from math import sqrt

input = stdin.readline

n,w,h=map(int,input().split())
a=w*w+h*h
for _ in range(n):
    t = int(input())
    if t*t<=a:
        print('DA')
    else:
        print('NE')