from sys import stdin,maxsize


input = stdin.readline

n = int(input())
a=b=0
for _ in range(n):
    p,q=map(int,input().split())
    if p==q:
        continue
    if p>q:
        a+=1
    else:
        b+=1
print(a,b)