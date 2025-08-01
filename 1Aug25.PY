class Solution:
    
    vowels={"a","e","i","o","u"}
    
    def count(self,string):
        v=sum(1 for ch in string if ch in self.vowels)
        c=len(string)-v
        return v,c
    
    def countBalanced(self, arr):
        preSum={0:1}
        v=c=ans=0
        for s in arr:
            dv,dc=self.count(s)
            v+=dv
            c+=dc
            diff=v-c
            ans+=preSum.get(diff,0)
            preSum[diff]=preSum.get(diff,0)+1
        return ans
        # code here
        
