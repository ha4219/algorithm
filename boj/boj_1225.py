from sys import stdin


input = stdin.readline

s,m=input().split()
def stn(s):
    res = 0
    for c in s:
        res += int(c)
    return res
print(stn(s)*stn(m))