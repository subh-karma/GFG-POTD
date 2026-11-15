class Solution:
    def subsequenceSum(self, s):
        mod=10**9+7
        ret=0
        lth=len(s)
        for c in s:
            ret=(ret+int(c)*pow(2,lth-1,mod))%mod
        return ret
        """code here"""
