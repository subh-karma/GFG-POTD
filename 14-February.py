class Solution:
    def correctBST(self, root):
    # your code here
        self.f=self.s=self.prev=None
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            if self.prev and self.prev.data>node.data:
                if not self.f:
                    self.f=self.prev
                self.s=node
            self.prev=node
            inorder(node.right)
        inorder(root)
        if self.f and self.s:
            self.f.data, self.s.data = self.s.data, self.f.data
