'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''
        
class Solution:
    def absDiff(self, root):
            MAX = 10 ** 6

            def dfs(node: Node) -> tuple[int, int]:
                mini = maxi = node.data
                min_abs_diff = MAX
                if node.left:
                    mini, left_max, left_diff = dfs(node.left)
                    min_abs_diff = min(left_diff, node.data - left_max)
                if node.right:
                    right_min, maxi, right_diff = dfs(node.right)
                    min_abs_diff = min(min_abs_diff, right_diff, right_min - node.data)
                return mini, maxi, min_abs_diff

            return dfs(root)[2]
        # code here
        
