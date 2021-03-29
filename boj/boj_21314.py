from sys import stdin,setrecursionlimit


setrecursionlimit(10**6)
input = stdin.readline


s = input().strip()

def fmax(s):
    sl = len(s)
    m = 0
    k = 0
    for i in range(sl):
        if s[i]=='M':
            m+=1
        else:
            k+=1
            break
    if k==0:
        return '1'*m
    return '5'+'0'*m+fmax(s[i+1:])

def fmin(s):
    sl = len(s)
    res = ''
    m = 0
    k = 0
    for i in range(sl):
        if s[i]=='M':
            m+=1
        else:
            if m>1:
                res += '1'+'0'*(m-1)
                m = 0
            if m==1:
                res += '1'
                m = 0
            res += '5'
    if m:
        res += '1'+'0'*(m-1)
    return res
            

print(fmax(s))
print(fmin(s))