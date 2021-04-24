from sys import stdin


input = stdin.readline

s = input().strip()

d = [0] * 26
for c in s:
    d[ord(c)-ord('A')] += 1

def solve():
    r = 0
    idx = 0
    for i in range(26):
        if not r and d[i]%2:
            r = 1
            idx = i
            d[i] -= 1
        elif r and d[i]%2:
            print("I'm Sorry Hansoo")
            return 0
    left = ''
    for i in range(26):
        for j in range(d[i]//2):
            left += chr(ord('A')+i)
    if r:
        print(left+chr(ord('A')+idx)+left[::-1])
    else:
        print(left+left[::-1])
    return 1
solve()