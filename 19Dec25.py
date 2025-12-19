class Solution:
    def findMoves(self, chairs, passengers):
        chairs.sort()
        passengers.sort()
        ans=0
        for c,p in zip(chairs,passengers):
            ans+=(abs(c-p))
        return ans
        # code here
        
