class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #code here
        slow = head
        fast = head.next
        if not fast:
            return 0
        found_cycle = False
        while fast and fast.next:
            if slow == fast:
                found_cycle = True
                break
            slow = slow.next
            fast = fast.next.next
        
        if not found_cycle:
            return 0
        
        cycle_node = slow
        cur = slow.next
        res = 1
        while cur != cycle_node:
            cur = cur.next
            res += 1
        return res
