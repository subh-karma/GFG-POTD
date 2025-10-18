'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
     def findMedian(self, root):
        
        def get_size(node):
            if node is None:
                return 0
            return 1 + get_size(node.left) + get_size(node.right)
        
        median_i = (get_size(root) + 1) // 2
        
        def dfs(node, less_count=0):
            if node is None:
                return less_count, -1
            less_count, median = dfs(node.left, less_count)
            if median != -1:
                return less_count, median
            less_count += 1
            if less_count == median_i:
                return less_count, node.data
            return dfs(node.right, less_count)
        
        return dfs(root)[1]
        # code here
