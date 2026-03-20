'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    
    def findPreSuc(self, root, key):
        def findPreSucUtil(root, pre, suc, key):
            if not root: return
        
            findPreSucUtil(root.left, pre, suc, key)
            if root.data < key:
                pre.data = root.data
            if not suc.data and root.data > key:
                suc.data = root.data
            findPreSucUtil(root.right, pre, suc, key)

        pre = Node(None)
        suc = Node(None)
        findPreSucUtil(root, pre, suc, key)
        pre.data = pre.data if pre.data else -1
        suc.data = suc.data if suc.data else -1
        return (pre, suc)
        # code here
