class Solution:  
    def findTarget(self, root, target):  
        seen = set()  
        
        def find(node):  
            if not node:  
                return False  
            
            complement = target - node.data  
            if complement in seen:  
                return True  
            
            seen.add(node.data)  
            return find(node.left) or find(node.right)  
        return find(root)
        # your code here.
