from sys import stdin


input = stdin.readline

s = input()[:-1]
m = input()[:-1]

def solve(s,m):
    res = 0
    sl,ml=len(s),len(m)
    start = 0
    while start+ml<=sl:
        cur = 1
        for i in range(ml):
            if s[start+i]!=m[i]:
                start+=1
                cur = 0
                break
        if cur:
            res += 1
            start += ml
    return res
print(solve(s,m))