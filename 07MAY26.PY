# Definition for Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    def isSubTree(self, root1, root2):
        def ok(n1,n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.data!=n2.data:
                return False
            return ok(n1.left,n2.left) and ok(n1.right,n2.right)
        def dfs(cur=root1):
            nonlocal root2
            if not cur:
                return False
            if ok(cur,root2):
                return True
            return dfs(cur.left) or dfs(cur.right)
        return dfs()


        # code here
