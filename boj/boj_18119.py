from sys import stdin


input = stdin.readline

n, m = map(int, input().split())
a = [0] * n
init = 0
for i in range(n):
    word = input().strip()
    word_bit = 0
    for c in word:
        word_bit |= 1<<(ord(c)-ord('a'))
    a[i] = word_bit
    init |= word_bit

def check(bit):
    res = 0
    for i in range(n):
        if bit&a[i]==a[i]:
            res += 1
    return res

for _ in range(m):
    condition, val = map(str,input().split())
    if condition=='1':
        init &= ~(1<<(ord(val)-ord('a')))
    else:
        init |= (1<<(ord(val)-ord('a')))
    print(check(init))