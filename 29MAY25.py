class Solution:
    def sumOfLongRootToLeafPath(self, root):
        #code here
        s0, l0 = 0, 0
        def dfs(n, s, l):
            nonlocal s0, l0
            if not n:
                return
            s += n.data
            l += 1
            if l > l0 or (l == l0) and s > s0:
                l0 = l
                s0 = s

            dfs(n.left, s, l)
            dfs(n.right, s, l)
        
        dfs(root, 0, 0)
        return s0
