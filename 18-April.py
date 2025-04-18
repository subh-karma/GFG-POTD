#User function Template for python3
class Node:
    def __init__(self):
        self.store = [None]*26
        self.done = False
    
    def insert(self, word):
        node = self
        for ch in word:
            key = ord(ch) - ord('a')
            if node.store[key] is None:
                node.store[key] = Node()
            node = node.store[key]
        node.done = True
    
    def search(self, word):
        node = self
        for ch in word:
            key = ord(ch) - ord('a')
            if node.store[key] is None:
                return False
            node = node.store[key]
        return node.done
    
    def is_prefix(self, word):
        node = self
        for ch in word:
            key = ord(ch) - ord('a')
            if node.store[key] is None:
                return False
            node = node.store[key]
        return True
            
    
class Trie:
    def __init__(self):
        # implement Trie
        self.root = Node()
        
    def insert(self, word: str):
       # insert word into Trie
        self.root.insert(word)
            

    def search(self, word: str) -> bool:
         # search word in the Trie
         return self.root.search(word)

    def isPrefix(self, word: str) -> bool:
         # search prefix word in the Trie
         return self.root.is_prefix(word)

