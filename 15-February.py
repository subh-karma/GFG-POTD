'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def LCA(self, root, n1, n2):
        # your code here
        if not root:
            return None
        if root ==n1 or root == n2:
            return root
        l = self.LCA(root.left, n1, n2)
        r = self.LCA(root.right, n1, n2)
        if l and r:
            return root
        return l if l else r
        
    

