class Solution:
    def segregate(self, head):
        #sam
        def insert(curr,count,n):
            for i in range(count):
                curr.data = n
                curr = curr.next
            return curr
        count_zero = 0
        count_one = 0
        count_two = 0
        curr = head
        while curr:
            if curr.data==0:
                count_zero +=1
            elif curr.data==1:
                count_one +=1
            else:
                count_two += 1
            curr = curr.next
        
        curr = head
        curr = insert(curr,count_zero,0)
        curr = insert(curr,count_one,1)
        curr = insert(curr,count_two,2)
        return head
