class Node:
    def __init__(self, ref = None):
        self.ref = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char in cur.ref:
                cur = cur.ref[char]
            else:
                cur.ref[char] = Node()
                cur = cur.ref[char]
            
        cur.end = True



    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char in cur.ref:
                cur = cur.ref[char]
            else:
                return False

        if cur.end:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char in cur.ref:
                cur = cur.ref[char]
            else:
                return False
        
        return True
        
        