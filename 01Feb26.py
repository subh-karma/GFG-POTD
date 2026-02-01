class Solution:
    def maxOfSubarrays(self, arr, k):
        from collections import deque
        ret=[]
        stk=deque()
        for ix in range(len(arr)):
            while stk and stk[0]<=ix-k:
                stk.popleft()
            while stk and arr[stk[-1]]<=arr[ix]:
                stk.pop()
            stk.append(ix)
            if ix>=k-1:
                ret.append(arr[stk[0]])
        return ret


        # code here
