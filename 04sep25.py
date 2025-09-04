class Solution:
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
    
        def reverse(head):
            prev, node = None, head
            for _ in range(k):
                node.next, node, prev = prev, node.next, node
                if node is None:
                    return prev
            head.next = reverse(node)
            return prev
        
        return reverse(head)
