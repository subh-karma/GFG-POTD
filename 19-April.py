#User function Template for python3
class TrieNode:
    def __init__(self):
        self.child=[None]*2
        self.val=0
        
class Trie:
    def __init__(self,n):
        self.root=TrieNode()
        self.n=n
    
    def add(self,num):
        cur=self.root
        for k in range(self.n,-1,-1):
            d=1 if num&(1<<k) else 0
            if not cur.child[d]:
                cur.child[d]=TrieNode()
            cur=cur.child[d]
        cur.val=num    
    
    def check(self,num):
        cur=self.root
        for k in range(self.n,-1,-1):
            d=1 if num&(1<<k) else 0
            if cur.child[(d+1)%2]:
                cur=cur.child[(d+1)%2]
            else:
                cur=cur.child[d]
        return cur.val^num 
    
            
        
class Solution:
    def maxXor(self, arr):
        #code here
        mx=len(bin(max(arr)))-2
        trie=Trie(mx)
        
        for el in arr:
            trie.add(el)
        
        res=0
        for el in arr:
            res=max(res,trie.check(el))
        
        return res
        
