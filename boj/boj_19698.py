from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

input = stdin.readline

n,w,h,l=map(int,input().split())
print(min(n,(w//l)*(h//l)))