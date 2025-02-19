class Solution:
    def mergeKLists(self, arr):
        dummy=Node(None)
        cur=dummy
        q=[(x.data,x,) for x in arr]
        import heapq
        heapq.heapify(q)
        while q:
            ele=heapq.heappop(q)[1]
            if ele:
                cur.next=ele
                if ele.next:
                    heapq.heappush(q,(ele.next.data,ele.next,))
                cur=cur.next
        return dummy.next
            
