class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove_front(self):
        if self.head.next == self.tail:
            return None 
        
        n = self.head.next
        self.head.next = n.next
        n.next.prev = self.head
        n.next = n.prev = None
        return n
        
    def append(self, v):
        n = Node(v)
        self.tail.prev.next = n 
        n.prev = self.tail.prev 
        n.next = self.tail
        self.tail.prev = n
        
class Solution:
    def rearrangeQueue(self, q):
        #code here 
        n = len(q)
        
        i, j = 0, n//2
        mlist = LinkedList()
        
        while j < n:
            node = mlist.remove_front()
            if node is not None:
                mlist.append(q[i])
                q[i] = node.value
            i += 1
            mlist.append(q[i])
            q[i] = q[j]
            i += 1
            j += 1
        return q
