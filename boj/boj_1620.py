from sys import stdin


input = stdin.readline

n,m=map(int,input().split())
s = {}

for i in range(1,n+1):
    t = input().strip()
    s[t]=i
    s[i]=t

for _ in range(m):
    t=input().strip()
    try:
        t = int(t)
        print(s[t])
    except:
        print(s[t])