from sys import stdin


input = stdin.readline

a=input()[:-1]
b=input()[:-1]


def getp(s):
    sl = len(s)
    pi = [0] * sl
    begin,matched=1,0
    while begin+matched<sl:
        if s[begin+matched]==s[matched]:
            matched+=1
            pi[begin+matched-1]=matched
        else:
            if matched==0:
                begin+=1
            else:
                begin+=matched-pi[matched-1]
                matched=pi[matched-1]
    return pi

def kmp(a,b):
    n,m=len(a),len(b)
    ret = []
    pi=getp(b)
    matched = 0
    for i in range(n):
        while matched>0 and a[i]!=b[matched]:
            matched=pi[matched-1]
        if a[i]==b[matched]:
            matched+=1
            if matched==m:
                ret.append(i-m+1)
                matched=pi[matched-1]
    return ret

res = kmp(a,b)
print(len(res))
for i in res:
    print(i+1)
