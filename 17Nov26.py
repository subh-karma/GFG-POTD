class Solution:
    def findPattern(self, s):
        prv='y'
        cnt=0
        for c in s:
            cnt+=1 if c=='x' else -1
            if c=='x' and c!=prv and cnt!=1:
                return False
            prv=c
        return cnt==0


        # code here
        
