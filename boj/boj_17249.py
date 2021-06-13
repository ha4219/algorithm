from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

s = input().strip()
t = '(^0^)'
tl = len(t)
x = s.find(t)
print(s[:x].count('@'),s[x+tl:].count('@'))