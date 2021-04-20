from sys import stdin,maxsize
from math import sqrt

input = stdin.readline

a=list(map(int,input().split()))
b=list(map(int,input().split()))
l = len(a)
aa=bb=0
w = -1
for i in range(l):
    if a[i]>b[i]:
        aa+=3
        w = 1
    elif a[i]==b[i]:
        aa+=1
        bb+=1
    else:
        bb+=3
        w = 0

print(aa,bb)
if aa==bb and aa==10:
    print('D')
elif aa>bb or w:
    print('A')
else:
    print('B')