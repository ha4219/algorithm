from sys import stdin, maxsize, setrecursionlimit


input = stdin.readline

a = int(input())
b = int(input())
c = int(input())

d = [0] * 10

for c in str(a*b*c):
    d[int(c)] += 1
print('\n'.join(map(str, d)))