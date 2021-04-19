from sys import stdin


input = stdin.readline

res = [0] * 10
n = int(input())

def f(n, t):
    while n:
        res[n%10]+=t
        n//=10

def solve(a,b,t):
    while a%10!=0 and a<=b:
        f(a,t)
        a+=1
    if a>b:
        return
    while b%10!=9 and b>=a:
        f(b,t)
        b-=1
    c=b//10-a//10+1
    for i in range(10):
        res[i]+=c*t
    solve(a//10,b//10,t*10)
solve(1,n,1)
print(*res)