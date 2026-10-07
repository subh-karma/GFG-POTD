'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:        
    def maxPathSum(self, root):
            ans = float('-inf')

            def dfs(n):
                nonlocal ans

                if not n:
                    return float('-inf')

                if not n.left and not n.right:
                    return n.data

                left = dfs(n.left)
                right = dfs(n.right)

                # A valid leaf-to-leaf path can only pass through
                # n if both sides exist.
                if n.left and n.right:
                    ans = max(ans, left + n.data + right)

                # Return the best leaf-to-n path to the parent.
                return n.data + max(left, right)

            dfs(root)
            return -1 if ans == float('-inf') else ans
        # code here
        
