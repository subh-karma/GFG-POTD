#User function Template for python3


'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque

class Solution:
    # Function to serialize a tree and return a list containing nodes of the tree.
    def serialize(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                result.append(node.data)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('N')  # Placeholder for null
            
        return result

    # Function to deserialize a list and construct the tree.
    def deSerialize(self, arr):
        if not arr or arr[0] == 'N':
            return None
        
        root = Node(arr[0])
        queue = deque([root])
        i = 1
        
        while queue and i < len(arr):
            node = queue.popleft()
            
            # Assign left child
            if arr[i] != 'N':
                node.left = Node(arr[i])
                queue.append(node.left)
            i += 1
            
            # Assign right child
            if i < len(arr) and arr[i] != 'N':
                node.right = Node(arr[i])
                queue.append(node.right)
            i += 1
        
        return root

    
