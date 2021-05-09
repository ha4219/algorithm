from sys import stdin, maxsize


input = stdin.readline


s = input().strip()

def f(s):
    res = 0
    for c in s:
        res += int(c)
    return res

for c in s:
    print(f(str(ord(c)))*c)