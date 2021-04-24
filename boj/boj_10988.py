from sys import stdin


input = stdin.readline

def f(s):
    sl = len(s)
    mid = sl//2 if sl%2 else sl//2-1
    for i in range(mid+1):
        if s[i]!=s[sl-i-1]:
            return 0
    return 1

print(f(input().strip()))