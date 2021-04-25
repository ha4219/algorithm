from sys import stdin


input = stdin.readline


def solve(l,p,v):
    res = 0
    while v>0:
        if v>l:
            res += l
            v -= p
        else:
            res += v
            v -= v
    return res
i = 0
while 1:
    i += 1
    a,b,c=map(int,input().split())
    if a==b and b==c and c==0:
        break
    print('Case %d: %d'%(i, solve(a,b,c)))
