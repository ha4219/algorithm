from sys import stdin


input = stdin.readline

n = int(input())
for i in range(n):
    p,q=map(int,input().split())
    print('Case %d: %d'%(i+1,p+q))