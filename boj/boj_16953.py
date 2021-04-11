from sys import stdin
from collections import deque


input = stdin.readline

a,b=map(int,input().split())

q = deque()
q.append((int(b),1))


def bfs():
    while q:
        n,c = q.popleft()
        if n<a:
            continue
        if n==a:
            return c
        
        if n!=1 and n%10==1:
            q.append((n//10, c+1))
        if n%2==0:
            q.append((n//2, c+1))
    return -1
print(bfs())