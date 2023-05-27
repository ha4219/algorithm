from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations, permutations
import math


MAX = 17
MOD = 1000000007
setrecursionlimit(10**6)
input = stdin.readline

N = int(input().strip())
s = [input().strip() for _ in range(N)]

class Q:
    cnt = [0, 0]
    direction = 0 # 
    d = deque() # 0: wall, 1: ball

    def __init__(self) -> None:
        pass
    
    def rotate(self, right: bool):
        self.direction = (self.direction + 1) % 4 if right \
            else (self.direction - 1) % 4
        self.waterfall()

    def count(self, v: int):
        print(self.cnt[v])
    
    def pop(self):
        if self.d:
            v = self.d.pop()
            self.cnt[v] -= 1
            self.waterfall()

    def push(self, v: int):
        self.cnt[v] += 1
        self.d.appendleft(v)
        self.waterfall()

    def waterfall(self):
        if self.direction & 1:
            pop = self.d.pop if self.direction == 1 else self.d.popleft
            append = self.d.append if self.direction == 1 else self.d.appendleft
            while self.d:
                v = pop()
                self.cnt[v] -= 1
                if not v:
                    self.cnt[v] += 1
                    append(v)
                    break



def main():
    q = Q()

    for l in s:
        query = l.split()
        
        match query[0]:
            case 'push':
                q.push(1 if query[1] == 'b' else 0)
            case 'pop':
                q.pop()
            case 'count':
                q.count(1 if query[1] == 'b' else 0)
            case 'rotate':
                q.rotate(query[1] == 'r')
        # print(q.d)
    return


if __name__ == "__main__":
    main()
