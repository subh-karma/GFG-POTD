class Solution:
    def sortedInsert(self, head, x):
        newnode = Node(x)
        
        # Case when the list is empty
        if head is None:
            return newnode
        
        # Case when the new node needs to be inserted at the head
        if head.data >= x:
            newnode.next = head
            head.prev = newnode
            return newnode
        
        current = head
        while current.next is not None and current.next.data < x:
            current = current.next
        
        newnode.next = current.next
        if current.next is not None:
            current.next.prev = newnode
        current.next = newnode
        newnode.prev = current
        
        return head
