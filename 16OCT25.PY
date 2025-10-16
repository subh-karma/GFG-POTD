'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def removekeys(self, root, l, r):
        return self.fun(root, l, r)
        
    def fun(self, root, l, r):
        if root is None:
            return None

        ans = None
        if l <= root.data <= r:
            ans = Node(root.data)
            ans.left = self.fun(root.left, l, r)
            ans.right = self.fun(root.right, l, r)
        elif root.data < l:
            ans = self.fun(root.right, l, r)
        elif root.data > r:
            ans = self.fun(root.left, l, r)

        return ans
 
        #code here
