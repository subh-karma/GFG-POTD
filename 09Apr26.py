class Solution:
    def intersection(self,a, b):
        res = list(set(a).intersection(set(b)))
        res.sort()
        return res
        # code here
        a
