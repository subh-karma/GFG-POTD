from heapq import heappush,heappop
class Solution:
    def getMedian(self, arr):
        left = []
        right = []
        res = []
        for ele in arr:
            heappush(left, -ele)
            while left and right and -left[0]>right[0]:
                heappush(right, -heappop(left))
            while abs(len(left)-len(right))>1:
                if len(left)>len(right):
                    heappush(right, -heappop(left))
                else:
                    heappush(left, -heappop(right))
            if len(left)==len(right):
                res.append((-left[0]+right[0])/2)
            else:
                res.append(-left[0] if len(left)>len(right) else right[0])
        return res
