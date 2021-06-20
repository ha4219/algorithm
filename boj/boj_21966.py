from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
s = input().strip()

if n<=25:
    print(s)
else:
    t = s[11:-11]
    tt = t.find('.')
    if tt==-1 or len(t)-1==tt:
        print(s[:11]+'...'+s[-11:])
    else:
        print(s[:9]+'.'*6+s[-10:])