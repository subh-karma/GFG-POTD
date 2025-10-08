'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

'''

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def constructTree(self, pre, post):
        self.preIndex = 0
        n = len(pre)
        postIndexMap = {val: i for i, val in enumerate(post)}

        def build(lo, hi):
            if self.preIndex >= n or lo > hi:
                return None

            root = Node(pre[self.preIndex])
            self.preIndex += 1

            if lo == hi or self.preIndex >= n:
                return root

            next_val = pre[self.preIndex]
            mid = postIndexMap[next_val]

            root.left = build(lo, mid)
            root.right = build(mid + 1, hi - 1)

            return root

        return build(0, n - 1)
 
        # code here
        
