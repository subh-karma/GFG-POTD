class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        zero, one, two = Node(0), Node(0), Node(0)
        tz, to, tt = zero, one, two
        while head:
            v = head.data
            t = head
            head = head.next
            t.next = None
            
            match v:
                case 0:
                    tz.next = t
                    tz = tz.next
                case 1:
                    to.next = t
                    to = to.next
                case _:
                    tt.next = t
                    tt = tt.next
            
        to.next = two.next
        tz.next = one.next
        return zero.next
    
