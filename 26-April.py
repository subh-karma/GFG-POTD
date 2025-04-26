from collections import deque

class Solution:
    # Your Function Should return True/False
    def isHeap(self, root):
        if not root:
            return True
        
        queue = deque()
        queue.append(root)
        nullChildSeen = False
        
        while queue:
            node = queue.popleft()
            
            # Check left child
            if node.left:
                if nullChildSeen or node.data < node.left.data:
                    return False
                queue.append(node.left)
            else:
                nullChildSeen = True
            
            # Check right child
            if node.right:
                if nullChildSeen or node.data < node.right.data:
                    return False
                queue.append(node.right)
            else:
                nullChildSeen = True
        
        return True

