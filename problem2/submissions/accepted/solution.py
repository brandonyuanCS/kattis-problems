class Node:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, msg, n):
        curr = self.root
        for c in msg:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
            curr.count += n

    def check(self, phrase):
        curr = self.root
        for c in phrase:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.count

n = int(input())
tr = Trie()
for _ in range(n):
    cin = input().split()
    msg, cnt = cin[0], int(cin[1])
    tr.add(msg, cnt)
q = int(input())
for _ in range(q):
    phrase = input()
    print(tr.check(phrase))