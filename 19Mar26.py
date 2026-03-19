class Solution:
    def largestBst(self, root):
        # Helper function to find largest BST subtree
        def helper(node):
            if not node:
                return 0, float('inf'), float('-inf'), 0  # size, min, max, largest BST size
            
            l_size, l_min, l_max, l_bst = helper(node.left)
            r_size, r_min, r_max, r_bst = helper(node.right)
            
            if l_max < node.data < r_min:
                size = 1 + l_size + r_size
                return size, min(l_min, node.data), max(r_max, node.data), size
            else:
                return 1 + l_size + r_size, float('-inf'), float('inf'), max(l_bst, r_bst)
        
        return helper(root)[3]


        # Your code here
