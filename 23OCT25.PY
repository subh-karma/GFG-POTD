from heapq import *
import math
class Solution:
    def kClosest(self, points, k):
        heap=[]
        for i,j in points:
            formula=math.sqrt((i)**2+(j)**2)
            heappush(heap,[formula,[i,j]])
        ans=[]
        while k and heap:
            k-=1
            ans.append(heappop(heap)[1])
        return ans
        # code here
        
        
