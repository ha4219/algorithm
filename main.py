from sys import stdin


input = stdin.readline

MAX = 2000001
n = MAX
s = [0] * (n * 4)
p = int(input())

def update(i, v, node, nL, nR):
    if i < nL or i > nR:
        return s[node]
    if nL ==  nR:
        s[node] += v
        return s[node]
    m = (nL + nR) // 2
    s[node] = update(i,v,node*2,nL,m)+update(i,v,node*2+1,m+1,nR)
    return s[node]

def q(num, node, nL, nR):
    if nL == nR:
        return nL
    m = (nL + nR) // 2
    if num > s[node*2]:
        num -= s[node*2]
        return q(num, node*2+1,m+1,nR)
    return q(num, node*2, nL, m)

for i in range(1,p+1):
    l = list(map(int,input().split()))
    if l[0] == 1:
        update(l[1], 1, 1, 0, n-1)
    else:
        r  =q(l[1], 1, 0, n-1)
        print(r)
        update(r, -1, 1, 0, n-1)