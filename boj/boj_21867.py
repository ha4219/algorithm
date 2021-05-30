from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**6)
input = stdin.readline

t = int(input())
n = input().strip()
n=n.replace('J','')
n=n.replace('A','')
n=n.replace('V','')
if len(n):
    print(n)
else:
    print('nojava')