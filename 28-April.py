class Solution:
    #Function to return the maximum sum of non-adjacent nodes.
    def getMaxSum(self, root):
        
        def dfs(node):
            if node is None:
                return 0, 0
            ltake, lskip = dfs(node.left)
            rtake, rskip = dfs(node.right)
            take = lskip + node.data + rskip
            skip = max(ltake, lskip) + max(rtake, rskip)
            return take, skip
        
        return max(dfs(root))
