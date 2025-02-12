
class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        ans = [-1]  # Use a list to store the answer (mutable)
        k = [k]  # Convert k to a list to allow modification inside recursion
        self.inorder(root, k, ans)  # Start in-order traversal
        return ans[0]  # Return the k-th smallest element

    def inorder(self, root, k, ans):
        if not root:  # Base case: if the node is None, return
            return
        
        self.inorder(root.left, k, ans)  # Traverse left subtree
        
        k[0] -= 1  # Decrement k (tracking the number of visited nodes)
        if k[0] == 0:  
            ans[0] = root.data  # Store the k-th smallest value
            return
        
        self.inorder(root.right, k, ans) 
