from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

class Node:
    def __init__(self, key, data=None):
        self.c = {}
        self.s = key
        self.data = data
    
class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        current_node = self.head
        for c in string:
            if c not in current_node.c:
                current_node.c[c] = Node(c)
            current_node = current_node.c[c]
            if current_node.data:
                return 0
        current_node.data = string
        return 1
    
    def search(self, string):
        current_node = self.head

        for c in string:
            if c in current_node.c:
                current_node = current_node.c[c]
            else:
                return 0
        
        if current_node.data:
            return 1
        else:
            return 0
        
    def starts_with(self, prefix):
        current_node = self.head
        words = []
        for p in prefix:
            if p in current_node.c:
                current_node = current_node.c[p]
            else:
                return None
        current_node = [current_node]
        next_node = []
        while 1:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.c.values()))
            if len(next_node)!=0:
                current_node = next_node
                next_node = []
            else:
                break
        return words


n = int(input())
sl = int(input())
s = input().strip()
m = 'I' + 'OI'*n
ml = len(m)

res = 0
p = 0
i = 1
while i < sl-1:
    if s[i-1:i+2]=='IOI':
        p += 1
        if p==n:
            res += 1
            p -= 1
        i += 1
    else:
        p = 0
    i += 1
print(res)