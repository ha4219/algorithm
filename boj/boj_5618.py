from sys import stdin
from math import gcd


input = stdin.readline

n = int(input())
if n==2:
    a,b=map(int,input().split())
    g = gcd(a,b)
else:
    a,b,c=map(int,input().split())
    g = gcd(gcd(a,b),c)
s = set()
for i in range(1,int(g**0.5)+1):
    if g%i==0:
        s.add(i)
        s.add(g//i)
r = sorted(s)
print('\n'.join(map(str,r)))
