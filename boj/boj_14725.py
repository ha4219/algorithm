from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 27
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

# trie format


class Trie:
    def __init__(self):
        self.head = {}

    def insert(self, words):
        current = self.head

        for word in words:
            if word not in current:
                current[word] = {}
            current = current[word]
        current[-1] = True

    def solve(self, depth, current):
        if -1 in current:
            return
        sorted_current = sorted(current)

        for word in sorted_current:
            print('--' * depth + word)
            self.solve(depth+1, current[word])
        return


# 문자열을 연결해서 trie 로 해야함
n = int(input())
t = Trie()

for _ in range(n):
    s = list(input().split())
    s = s[1:]
    t.insert(s)


t.solve(0, t.head)
