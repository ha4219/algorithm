from sys import stdin,maxsize


input = stdin.readline

n = int(input())
l = list(map(int,input().split()))
v = list(map(int,input().split()))

res = v[0]*l[0]
prev = v[0]
for i in range(1,n-1):
    if prev>v[i]:
        prev=v[i]
    res += l[i]*prev
    
print(res)