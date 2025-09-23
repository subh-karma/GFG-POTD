from collections import deque

class Solution:
    def reverseQueue(self, q):
        # base case
        if not q:
            return q
        
        # pop front element
        front = q.popleft()
        
        # recursive call on remaining queue
        self.reverseQueue(q)
        
        # push popped element at the rear
        q.append(front)
        
        return q
        # code here
        
