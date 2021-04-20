from sys import stdin,maxsize


input = stdin.readline

n = int(input())
r = 5

for i in range(2,n+1):
    r = (r + i*5 - i*2+1)%45678
print(r)