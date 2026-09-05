class Solution:
    def longestSubseq(self, arr):
        prev = {}
        for a in arr:
            prev[a] = 1 + max(prev.get(a - 1, 0), prev.get(a + 1, 0))
        return max(prev.values())
            # code here
        
